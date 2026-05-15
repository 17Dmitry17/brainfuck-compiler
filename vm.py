from __future__ import annotations
import sys
from ast_nodes import ProgramNode, LoopNode, IncrNode, DecrNode, MoveRNode, MoveLNode, OutputNode, InputNode

class VM:

    def __init__(self) -> None:
        self.tape: list[int] = [0] * 30000
        self.ptr: int = 0

    def run(self, tree: ProgramNode) -> None:
        self._exec(tree.children)

    def _exec(self, nodes: list) -> None:
        for node in nodes:
            if isinstance(node, IncrNode):
                self.tape[self.ptr] = (self.tape[self.ptr] + node.count) % 256
            elif isinstance(node, DecrNode):
                self.tape[self.ptr] = (self.tape[self.ptr] - node.count) % 256
            elif isinstance(node, MoveRNode):
                self.ptr += node.count
                if self.ptr >= len(self.tape):
                    raise RuntimeError(f'Выход за правую границу ленты на позиции {node.pos}')
            elif isinstance(node, MoveLNode):
                self.ptr -= node.count
                if self.ptr < 0:
                    raise RuntimeError(f'Выход за левую границу ленты на позиции {node.pos}')
            elif isinstance(node, OutputNode):
                print(chr(self.tape[self.ptr]), end='', flush=True)
            elif isinstance(node, InputNode):
                char = sys.stdin.read(1)
                self.tape[self.ptr] = ord(char) if char else 0
            elif isinstance(node, LoopNode):
                while self.tape[self.ptr]:
                    self._exec(node.children)