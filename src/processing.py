def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    new_dict_list = [dic_t for dic_t in dict_list if dic_t["state"] == state]  # Новый список словарей по ключу
    return new_dict_list
