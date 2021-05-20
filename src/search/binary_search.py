from bisect import bisect_left, bisect_right
from typing import List


def is_ok(value_list: List[int], index: int, key: int) -> bool:
    # index が条件を満たすかどうか
    if value_list[index] >= key:
        return True
    else:
        return False


def binary_search(value_list: List[int], key: int) -> int:
    # 「index = 0」が条件を満たすこともあるので、初期値は -1
    left = -1

    # 「index = len(value_list) -1」が条件を満たさないこともあるので、初期値は len(A)
    right = len(value_list)

    while right - left > 1:
        mid = left + (right - left) // 2

        if is_ok(value_list, mid, key):
            right = mid
        else:
            left = mid

    # left は条件を満たさない最大の値、right は条件を満たす最小の値になっている
    return right


if __name__ == "__main__":
    arr = [10 * i for i in range(10)]
    key = 53
    r1 = binary_search(arr, key)

    # bisect_left ... 条件を満たす最小の値のうち，一番左ものを返す．
    # bisect_right ... 条件を満たす最小の値のうち，一番右のものを返す．
    l2 = bisect_left(arr, key)
    r2 = bisect_right(arr, key)

    assert r1 == l2 == r2
