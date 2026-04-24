from __future__ import annotations
import sys
from ast_nodes import ProgramNode, LoopNode, IncrNode, DecrNode, MoveRNode, MoveLNode, OutputNode, InputNode

# Настройка кодировки для корректного вывода в Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

_NODE_SYMBOLS = {
    IncrNode: "+",
    DecrNode: "-",
    MoveRNode: ">",
    MoveLNode: "<",
    OutputNode: ".",
    InputNode: ",",
    LoopNode: "[]",
}

def print_ast(node, prefix: str = "", is_last: bool = True) -> None:
    if isinstance(node, ProgramNode):
        print("Program")
        for i, child in enumerate(node.children):
            print_ast(child, prefix="    ", is_last=(i == len(node.children) - 1))
        return

    connector = "└── " if is_last else "├── "
    
    symbol = _NODE_SYMBOLS.get(type(node), "")
    name = type(node).__name__
    
    # Добавляем вывод count, если он есть и больше 1
    count_str = ""
    if hasattr(node, 'count') and node.count > 1:
        count_str = f" x{node.count}"
        
    if symbol:
        name = f"{name} ({symbol}){count_str}"
        
    pos = f" (pos={node.pos})"

    print(f"{prefix}{connector}{name}{pos}")

    if isinstance(node, LoopNode):
        extension = "    " if is_last else "│   "
        for i, child in enumerate(node.children):
            print_ast(child, prefix=prefix + extension, is_last=(i == len(node.children) - 1))