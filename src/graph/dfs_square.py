from collections import deque
from typing import List


def dfs(
    square: List[str],
    h: int,
    w: int,
    sh: int,
    sw: int,
    gh: int,
    gw: int,
) -> bool:
    """depth-first search
    Args:
        square: square maze
        h: the height of the square
        w: the width of the square
        sh, sw: the coordinate of the start point.
        gh, gw: the coordinate of the goal point.
    Return:
        res: whether the goal point can be reached or not.
    """
    visited = [[False] * w for _ in range(h)]
    visited[sh][sw] = True
    q = deque([(sh, sw)])

    while q:
        cur_h, cur_w = q.pop()

        if cur_h == gh and cur_w == gw:
            return True

        for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_h = cur_h + dh
            next_w = cur_w + dw

            if 0 <= next_h < h and 0 <= next_w < w:
                if visited[next_h][next_w]:
                    continue

                if square[next_h][next_w] == "." or square[next_h][next_w] == "g":
                    visited[next_h][next_w] = True
                    q.append((next_h, next_w))

    return False


if __name__ == "__main__":
    """Problem from atcoder
    https://atcoder.jp/contests/atc001/tasks/dfs_a
    """

    h, w = map(int, input().split())
    square = [input() for _ in range(h)]

    sh = 0
    sw = 0
    gh = 0
    gw = 0
    for i in range(h):
        for j in range(w):
            if square[i][j] == "s":
                sh = i
                sw = j
            elif square[i][j] == "g":
                gh = i
                gw = j

    res = dfs(square, h, w, sh, sw, gh, gw)
    if res:
        print("Yes")
    else:
        print("No")
