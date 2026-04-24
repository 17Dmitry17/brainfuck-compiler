from __future__ import annotations
from typing import List

from ast_nodes import (
    ProgramNode, LoopNode,
    IncrNode, DecrNode,
    MoveRNode, MoveLNode,
    OutputNode, InputNode,
)

# Пары взаимно отменяющихся команд
_OPPOSITES = {
    IncrNode: DecrNode,
    DecrNode: IncrNode,
    MoveRNode: MoveLNode,
    MoveLNode: MoveRNode,
}

# Узлы у которых есть поле count
_COUNTABLE = (IncrNode, DecrNode, MoveRNode, MoveLNode)


def optimize(tree: ProgramNode) -> ProgramNode:
    return ProgramNode(children=_optimize_block(tree.children))


def _optimize_block(nodes: list) -> list:
    result = _merge_runs(_optimize_children(nodes))
    result = _cancel_opposites(result)
    return result


def _optimize_children(nodes: list) -> list:
    out = []
    for node in nodes:
        if isinstance(node, LoopNode):
            children = _optimize_block(node.children)
            if children:  # оптимизация 3: пустые циклы удаляем
                out.append(LoopNode(children=children, pos=node.pos))
        else:
            out.append(node)
    return out


def _merge_runs(nodes: list) -> list:
    """Оптимизация 1: схлопываем одинаковые команды подряд в один узел с count."""
    if not nodes:
        return []

    result = []
    current = nodes[0]

    for node in nodes[1:]:
        if (
            isinstance(node, _COUNTABLE)
            and type(node) is type(current)
        ):
            # Суммируем count в текущий узел
            current = type(current)(pos=current.pos, count=current.count + node.count)
        else:
            result.append(current)
            current = node

    result.append(current)
    return result


def _cancel_opposites(nodes: list) -> list:
    """Оптимизация 2: удаляем взаимно отменяющиеся пары (+- и ><)."""
    changed = True
    while changed:
        changed = False
        result = []
        i = 0
        while i < len(nodes):
            node = nodes[i]
            if (
                i + 1 < len(nodes)
                and isinstance(node, _COUNTABLE)
                and type(nodes[i + 1]) is _OPPOSITES.get(type(node))
            ):
                a, b = node, nodes[i + 1]
                diff = a.count - b.count
                if diff > 0:
                    result.append(type(a)(pos=a.pos, count=diff))
                elif diff < 0:
                    result.append(type(b)(pos=b.pos, count=-diff))
                # diff == 0 — оба узла исчезают
                i += 2
                changed = True
            else:
                result.append(node)
                i += 1
        nodes = result

    return nodes
