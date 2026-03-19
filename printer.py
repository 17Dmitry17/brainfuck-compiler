from __future__ import annotations
from ast_nodes import ProgramNode, LoopNode

def print_ast(node, prefix: str = "", is_last: bool = True) -> None:
    if isinstance(node, ProgramNode):
        print("Program")
        for i, child in enumerate(node.children):
            print_ast(child, prefix="", is_last=(i == len(node.children) - 1))
        return

    connector = "└── " if is_last else "├── "
    name = type(node).__name__
    pos = f" (pos={node.pos})"

    print(f"{prefix}{connector}{name}{pos}")

    if isinstance(node, LoopNode):
        extension = "    " if is_last else "│   "
        for i, child in enumerate(node.children):
            print_ast(child, prefix=prefix + extension, is_last=(i == len(node.children) - 1))