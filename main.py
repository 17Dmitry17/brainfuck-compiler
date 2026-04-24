from __future__ import annotations
import sys
import argparse
from lexer import tokenize
from parser import parse
from printer import print_ast
from codegen import generate

def main() -> None:
    parser = argparse.ArgumentParser(description="Brainfuck Compiler")
    parser.add_argument("input", help="Input .bf file")
    parser.add_argument("-o", "--output", help="Output .py file", default="out.py")
    parser.add_argument("--no-ast", action="store_true", help="Don't print AST")
    
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found")
        sys.exit(1)

    # 1. Токенизация
    tokens = tokenize(source)

    # 2. Парсинг
    try:
        tree = parse(tokens)
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        sys.exit(1)

    # 3. Вывод AST
    if not args.no_ast:
        print("AST Structure:")
        print_ast(tree)
        print("-" * 20)

    # 4. Генерация кода
    code = generate(tree)
    
    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Success! Python code generated in '{args.output}'")
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
