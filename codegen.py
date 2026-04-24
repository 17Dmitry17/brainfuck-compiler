from __future__ import annotations
from ast_nodes import (
    ProgramNode, LoopNode, IncrNode, DecrNode,
    MoveRNode, MoveLNode, OutputNode, InputNode
)

def generate(tree: ProgramNode) -> str:
    lines = [
        "tape = [0] * 30000",
        "ptr = 0",
        ""
    ]

    def visit(node, indent_level: int):
        indent = "    " * indent_level
        
        if isinstance(node, IncrNode):
            lines.append(f"{indent}tape[ptr] += 1")
        elif isinstance(node, DecrNode):
            lines.append(f"{indent}tape[ptr] -= 1")
        elif isinstance(node, MoveRNode):
            lines.append(f"{indent}ptr += 1")
        elif isinstance(node, MoveLNode):
            lines.append(f"{indent}ptr -= 1")
        elif isinstance(node, OutputNode):
            lines.append(f"{indent}print(chr(tape[ptr]), end=\"\")")
        elif isinstance(node, InputNode):
            lines.append(f"{indent}tape[ptr] = ord(input()[0])")
        elif isinstance(node, LoopNode):
            lines.append(f"{indent}while tape[ptr]:")
            if not node.children:
                lines.append(f"{indent}    pass")
            for child in node.children:
                visit(child, indent_level + 1)
        elif isinstance(node, ProgramNode):
            for child in node.children:
                visit(child, indent_level)

    visit(tree, 0)
    return "\n".join(lines)
