"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""

import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    my_dict = dict()

    @functools.wraps(func)
    def wrapper(*args):
        if args not in my_dict:
            my_dict[args] = func(*args)
        return my_dict[args]
    return wrapper


@cache
def funct(a, b):
    return (a ** b) ** 2


@functools.lru_cache
def functa(a, b):
    return (a ** b) ** 2