from __future__ import annotations
import sys
import argparse
from lexer import tokenize
from parser import parse
from semantic import analyse
from optimizer import optimize
from printer import print_ast
from codegen import generate

def main() -> None:
    parser = argparse.ArgumentParser(
        description="BF-Compiler: Полный цикл компиляции Brainfuck"
    )
    parser.add_argument("input", help="Исходный файл .bf")
    parser.add_argument("-o", "--output", default="out.py", help="Выходной Python файл")
    parser.add_argument("--ast", action="store_true", help="Показать AST дерево")
    
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8-sig") as f:
            source = f.read()
    except UnicodeDecodeError:
        try:
            with open(args.input, "r", encoding="cp1251") as f:
                source = f.read()
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            sys.exit(1)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input}' не найден")
        sys.exit(1)

    tokens = tokenize(source)

    try:
        tree = parse(tokens)
    except SyntaxError as e:
        print(f"Ошибка синтаксиса: {e}")
        sys.exit(1)

    reports = analyse(tree)
    has_errors = False
    for msg in reports:
        print(msg)
        if msg.startswith("Ошибка"):
            has_errors = True
    
    if has_errors:
        print("Компиляция прервана из-за семантических ошибок.")
        sys.exit(1)

    tree = optimize(tree)

    if args.ast:
        print("\n--- Оптимизированное AST ---")
        print_ast(tree)
        print("----------------------------\n")

    code = generate(tree)
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(code)
    
    print(f"Готово! Результат сохранен в {args.output}")

if __name__ == "__main__":
    main()
