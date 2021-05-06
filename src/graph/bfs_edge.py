from typing import List, Tuple

from connected import deque


def bfs(
    edges: List[List[Tuple[int, int]]],
    n_nodes: int,
    start: int,
    goal: int,
) -> int:
    """breadth-first search
    Args:
        edges: edges[i] is the list of the node connected to node i and the cost.
        n_nodes: the number of nodes.
        start: the index of the start.
        goal: the index of the goal.
    Return:
        res: the minimum number of moves. if -1, then the goal is unreachable.
    """
    costs = [10 ** 9] * n_nodes
    costs[start] = 0
    q = deque([(start, 0)])

    while q:
        i, cur_cost = q.popleft()

        if costs[i] < cur_cost:
            continue

        for j, cost in edges[i]:
            next_cost = cur_cost + cost
            if next_cost < costs[j]:
                costs[j] = next_cost
                q.append((j, next_cost))

    return costs[goal]
