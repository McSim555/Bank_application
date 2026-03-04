def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    new_dict_list = [dict for dict in dict_list if dict["state"] == state]  # Новый список словарей по ключу
    return new_dict_list
