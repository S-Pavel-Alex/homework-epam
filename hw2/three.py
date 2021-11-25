from itertools import combinations
from typing import Any, List


def combinat(*args: List[Any]) -> List[List]:
    """function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one."""
    all_list = []
    final_list = []
    ar_len = len(args)
    if ar_len == 1:
        return args[0]
    for i in range(ar_len):
        all_list += args[i]
    combo = list(combinations(all_list, ar_len))
    finish = list(map(lambda x: list(x), combo))
    for i in finish:
        if i not in args:
            final_list.append(i)
    return final_list