# Built-in modules
from os import system

def clear_screen() -> None:
    system("cls||clear")


def join_with_and(lst: list[str]) -> str:
    if len(lst) == 1: return lst[0]

    return ', '.join(lst[:-1]) + ' and ' + lst[-1]
