"""
AST nodes for the BrainFuck compiler.

Every node stores the source position (pos) for error reporting.
ProgramNode and LoopNode are composite nodes that hold child nodes.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class ProgramNode:
    """Root node of the AST — wraps the entire program."""
    children: List[object] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"ProgramNode(children={self.children!r})"


@dataclass
class LoopNode:
    """[...] loop construct."""
    children: List[object]
    pos: int  # position of the opening '['

    def __repr__(self) -> str:
        return f"LoopNode(pos={self.pos}, children={self.children!r})"


@dataclass
class IncrNode:
    """'+' — increment the current cell."""
    pos: int

    def __repr__(self) -> str:
        return f"IncrNode(pos={self.pos})"


@dataclass
class DecrNode:
    """'-' — decrement the current cell."""
    pos: int

    def __repr__(self) -> str:
        return f"DecrNode(pos={self.pos})"


@dataclass
class MoveRNode:
    """'>' — move the data pointer one cell to the right."""
    pos: int

    def __repr__(self) -> str:
        return f"MoveRNode(pos={self.pos})"


@dataclass
class MoveLNode:
    """'<' — move the data pointer one cell to the left."""
    pos: int

    def __repr__(self) -> str:
        return f"MoveLNode(pos={self.pos})"


@dataclass
class OutputNode:
    """'.' — output the byte at the current cell."""
    pos: int

    def __repr__(self) -> str:
        return f"OutputNode(pos={self.pos})"


@dataclass
class InputNode:
    """',' — read one byte into the current cell."""
    pos: int

    def __repr__(self) -> str:
        return f"InputNode(pos={self.pos})"
