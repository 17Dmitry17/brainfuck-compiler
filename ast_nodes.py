from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class ProgramNode:
    children: List[object] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"ProgramNode(children={self.children!r})"


@dataclass
class LoopNode:
    children: List[object]
    pos: int

    def __repr__(self) -> str:
        return f"LoopNode(pos={self.pos}, children={self.children!r})"


@dataclass
class IncrNode:
    pos: int
    count: int = 1

    def __repr__(self) -> str:
        return f"IncrNode(pos={self.pos}, count={self.count})"


@dataclass
class DecrNode:
    pos: int
    count: int = 1

    def __repr__(self) -> str:
        return f"DecrNode(pos={self.pos}, count={self.count})"


@dataclass
class MoveRNode:
    pos: int
    count: int = 1

    def __repr__(self) -> str:
        return f"MoveRNode(pos={self.pos}, count={self.count})"


@dataclass
class MoveLNode:
    pos: int
    count: int = 1

    def __repr__(self) -> str:
        return f"MoveLNode(pos={self.pos}, count={self.count})"


@dataclass
class OutputNode:
    pos: int

    def __repr__(self) -> str:
        return f"OutputNode(pos={self.pos})"


@dataclass
class InputNode:
    pos: int

    def __repr__(self) -> str:
        return f"InputNode(pos={self.pos})"
