from typing import Any


def filter_by_state(dict_list: list, state: Any = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    new_dict_list = [x for x in dict_list if dict_list[state] == state]  # Новый список словарей по ключу
    return new_dict_list
