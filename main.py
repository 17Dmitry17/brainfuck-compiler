from __future__ import annotations
import sys
import argparse
from lexer import tokenize
from parser import parse
from printer import print_ast
from codegen import generate

def compile_brainfuck(input_path: str, output_path: str, show_ast: bool) -> None:
    """Оркестратор процесса компиляции."""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"[-] Ошибка: Файл '{input_path}' не найден.")
        sys.exit(1)

    print(f"[*] Чтение файла: {input_path}")
    
    # 1. Лексический анализ
    tokens = tokenize(source)
    print(f"[*] Токенизация завершена. Найдено команд: {len(tokens)}")

    # 2. Синтаксический анализ
    try:
        tree = parse(tokens)
    except SyntaxError as e:
        print(f"[-] Синтаксическая ошибка: {e}")
        sys.exit(1)
    print("[*] AST дерево успешно построено.")

    # 3. Визуализация (по желанию)
    if show_ast:
        print("\n--- СТРУКТУРА AST ---")
        print_ast(tree)
        print("---------------------\n")

    # 4. Генерация кода
    print(f"[*] Генерация исполняемого кода...")
    code = generate(tree)
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[+] Успех! Скомпилированный код сохранен в: {output_path}")
    except IOError as e:
        print(f"[-] Ошибка при записи файла: {e}")
        sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(
        description="BF-Compiler: Транслятор Brainfuck в исполняемый Python-код"
    )
    parser.add_argument("input", help="Путь к исходному файлу .bf")
    parser.add_argument(
        "-o", "--output", 
        default="compiled.py", 
        help="Путь для сохранения результата (по умолчанию: compiled.py)"
    )
    parser.add_argument(
        "--ast", 
        action="store_true", 
        help="Вывести AST дерево в консоль"
    )
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
        
    args = parser.parse_args()
    compile_brainfuck(args.input, args.output, args.ast)

if __name__ == "__main__":
    main()
