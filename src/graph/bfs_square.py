from collections import deque
from typing import List


def bfs(
    square: List[str],
    h: int,
    w: int,
    sh: int,
    sw: int,
    gh: int,
    gw: int,
) -> int:
    """breadth-first search
    Args:
        square: square maze
        h: the height of the square
        w: the width of the square
        sh, sw: the coordinate of the start point.
        gh, gw: the coordinate of the goal point.
    Return:
        res: the minimum number of moves. if -1, then the goal is unreachable.
    """
    costs = [[-1] * w for _ in range(h)]
    costs[sh][sw] = 0
    q = deque([(sh, sw, 0)])

    while q:
        cur_h, cur_w, cur_cost = q.popleft()

        if costs[cur_h][cur_w] < cur_cost:
            continue

        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_h = cur_h + dh
            next_w = cur_w + dw

            if 0 <= next_h < h and 0 <= next_w < w:
                if costs[next_h][next_w] == -1 and square[next_h][next_w] == ".":
                    next_cost = cur_cost + 1
                    costs[next_h][next_w] = next_cost
                    q.append((next_h, next_w, next_cost))

    return costs[gh][gw]


if __name__ == "__main__":
    """Problem from AtCoder
    https://atcoder.jp/contests/abc007/tasks/abc007_3
    """
    h, w = map(int, input().split())
    sh, sw = map(lambda x: int(x) - 1, input().split())
    gh, gw = map(lambda x: int(x) - 1, input().split())
    square = [input() for _ in range(h)]

    res = bfs(square, h, w, sh, sw, gh, gw)
    print(res)
