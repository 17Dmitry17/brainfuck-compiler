"""
Recursive-descent parser for BrainFuck.

Usage:
    from parser import parse
    ast = parse(tokens)  # tokens: list[tuple[str, int]]
"""

from __future__ import annotations
from typing import List, Tuple

from ast_nodes import (
    ProgramNode, LoopNode,
    IncrNode, DecrNode,
    MoveRNode, MoveLNode,
    OutputNode, InputNode,
)

# Maps single-character commands to their leaf-node constructors.
_LEAF_MAP = {
    '+': IncrNode,
    '-': DecrNode,
    '>': MoveRNode,
    '<': MoveLNode,
    '.': OutputNode,
    ',': InputNode,
}


def parse(tokens: List[Tuple[str, int]]) -> ProgramNode:
    """
    Parse a flat token list into a ProgramNode AST.

    Parameters
    ----------
    tokens:
        Sequence of (command, position) pairs produced by the lexer.

    Returns
    -------
    ProgramNode
        The root node of the AST.

    Raises
    ------
    SyntaxError
        If a '[' is never closed or a ']' appears without a matching '['.
    """
    # Wrap the list in an iterator so the recursive helper can consume it
    # from a shared position without index arithmetic.
    iterator = iter(tokens)
    children = _parse_block(iterator, opening_pos=None)
    return ProgramNode(children=children)


def _parse_block(
    iterator,
    opening_pos: int | None,
) -> list:
    """
    Consume tokens from *iterator* and return a list of AST nodes.

    When *opening_pos* is not None the function is parsing the body of a
    loop and will stop (and return) upon seeing ']'.
    When *opening_pos* is None we are at the top level and ']' is an error.
    """
    children = []

    for cmd, pos in iterator:
        if cmd in _LEAF_MAP:
            children.append(_LEAF_MAP[cmd](pos=pos))

        elif cmd == '[':
            # Recurse to collect the loop body.
            body = _parse_block(iterator, opening_pos=pos)
            children.append(LoopNode(children=body, pos=pos))

        elif cmd == ']':
            if opening_pos is None:
                raise SyntaxError(
                    f"Unexpected ']' at position {pos}: "
                    "no matching '[' found."
                )
            # Normal end of a loop body — return to the caller.
            return children

        else:
            # The lexer should never emit unknown commands, but be safe.
            raise SyntaxError(
                f"Unknown token {cmd!r} at position {pos}."
            )

    # Exhausted all tokens.
    if opening_pos is not None:
        raise SyntaxError(
            f"Unclosed '[' at position {opening_pos}: "
            "end of input reached without a matching ']'."
        )

    return children
