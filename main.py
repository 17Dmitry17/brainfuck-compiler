from __future__ import annotations
import sys
from lexer import tokenize
from parser import parse
from printer import print_ast

def main() -> None:
    if len(sys.argv) < 2:
        print("Использование: python main.py <файл.bf>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{path}' не найден")
        sys.exit(1)

    tokens = tokenize(source)

    try:
        tree = parse(tokens)
    except SyntaxError as e:
        print(f"Синтаксическая ошибка: {e}")
        sys.exit(1)

    print_ast(tree)

if __name__ == "__main__":
    main()