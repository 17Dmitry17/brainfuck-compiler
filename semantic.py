from __future__ import annotations
from ast_nodes import ProgramNode, LoopNode, OutputNode


def analyse(tree: ProgramNode) -> list[str]:
    errors: list[str] = []

    _check_output(tree, errors)
    _walk(tree.children, depth=0, errors=errors)

    return errors


def _check_output(tree: ProgramNode, errors: list[str]) -> None:
    if not _has_output(tree.children):
        errors.append("Предупреждение: программа ничего не выводит (нет ни одной команды '.')")


def _has_output(nodes: list) -> bool:
    for node in nodes:
        if isinstance(node, OutputNode):
            return True
        if isinstance(node, LoopNode):
            if _has_output(node.children):
                return True
    return False


def _walk(nodes: list, depth: int, errors: list[str]) -> None:
    for node in nodes:
        if isinstance(node, LoopNode):
            if depth + 1 > 100:
                errors.append(
                    f"Ошибка: слишком глубокая вложенность циклов "
                    f"(больше 100 уровней) на позиции {node.pos}"
                )

            if len(node.children) == 0:
                errors.append(
                    f"Предупреждение: пустой цикл [] на позиции {node.pos}"
                )

            _walk(node.children, depth=depth + 1, errors=errors)