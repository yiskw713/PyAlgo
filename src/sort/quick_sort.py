from typing import List


def quick_sort(value_list: List[int]) -> List[int]:
    n = len(value_list)
    if n <= 1:
        return value_list

    pivot = value_list[0]

    left = [v for v in value_list if v < pivot]
    right = [v for v in value_list if v > pivot]
    pivots = [v for v in value_list if v == pivot]

    left_list = quick_sort(left)
    right_list = quick_sort(right)

    return left_list + pivots + right_list


if __name__ == "__main__":
    import random

    value_list = [i for i in range(10)]
    value_list += [5, 5]
    value_list = random.sample(value_list, len(value_list))

    res = quick_sort(value_list)
    print(res)
