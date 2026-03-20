from __future__ import annotations
from typing import List, Tuple

from ast_nodes import (
    ProgramNode, LoopNode,
    IncrNode, DecrNode,
    MoveRNode, MoveLNode,
    OutputNode, InputNode,
)

_LEAF_MAP = {
    '+': IncrNode,
    '-': DecrNode,
    '>': MoveRNode,
    '<': MoveLNode,
    '.': OutputNode,
    ',': InputNode,
}


def parse(tokens: List[Tuple[str, int]]) -> ProgramNode:
    iterator = iter(tokens)
    children = _parse_block(iterator, opening_pos=None)
    return ProgramNode(children=children)


def _parse_block(iterator, opening_pos: int | None) -> list:
    children = []

    for cmd, pos in iterator:
        if cmd in _LEAF_MAP:
            children.append(_LEAF_MAP[cmd](pos=pos))

        elif cmd == '[':
            body = _parse_block(iterator, opening_pos=pos)
            children.append(LoopNode(children=body, pos=pos))

        elif cmd == ']':
            if opening_pos is None:
                raise SyntaxError(
                    f"Unexpected ']' at position {pos}: "
                    "no matching '[' found."
                )
            return children

        else:
            raise SyntaxError(
                f"Unknown token {cmd!r} at position {pos}."
            )

    if opening_pos is not None:
        raise SyntaxError(
            f"Unclosed '[' at position {opening_pos}: "
            "end of input reached without a matching ']'."
        )

    return children
