from typing import Any

names = ["Yvor", "Wendell", "Hogan", "Sadella", "Yvor", "Sadella", "Hogan"]

def get_unique_names(names: list[str]) -> list[str]:
    """Функция, которая принимает список и возвращает уникальные элементы
       из него в виде списка. """

    unique_names = set(names).difference()
    return list(unique_names)


print(get_unique_names(names))