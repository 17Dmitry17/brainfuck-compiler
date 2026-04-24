from __future__ import annotations
import sys
from ast_nodes import (
    ProgramNode, LoopNode, IncrNode, DecrNode,
    MoveRNode, MoveLNode, OutputNode, InputNode
)

def generate(tree: ProgramNode) -> str:
    lines = [
        "import sys",
        "",
        "tape = [0] * 30000",
        "ptr = 0",
        ""
    ]

    def visit(node, indent_level: int):
        indent = "    " * indent_level
        
        if isinstance(node, IncrNode):
            lines.append(f"{indent}tape[ptr] += {node.count}")
        elif isinstance(node, DecrNode):
            lines.append(f"{indent}tape[ptr] -= {node.count}")
        elif isinstance(node, MoveRNode):
            lines.append(f"{indent}ptr += {node.count}")
        elif isinstance(node, MoveLNode):
            lines.append(f"{indent}ptr -= {node.count}")
        elif isinstance(node, OutputNode):
            # Добавим % 256 для безопасности вывода
            lines.append(f"{indent}print(chr(tape[ptr] % 256), end=\"\")")
        elif isinstance(node, InputNode):
            lines.append(f"{indent}try:")
            lines.append(f"{indent}    char = sys.stdin.read(1)")
            lines.append(f"{indent}    tape[ptr] = ord(char) if char else 0")
            lines.append(f"{indent}except EOFError:")
            lines.append(f"{indent}    pass")
        elif isinstance(node, LoopNode):
            lines.append(f"{indent}while tape[ptr]:")
            if not node.children:
                lines.append(f"{indent}    pass")
            else:
                for child in node.children:
                    visit(child, indent_level + 1)
        elif isinstance(node, ProgramNode):
            for child in node.children:
                visit(child, indent_level)

    visit(tree, 0)
    return "\n".join(lines)
