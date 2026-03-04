def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    new_dict_list = [dic_t for dic_t in dict_list if dic_t["state"] == state]  # Новый список словарей по ключу
    return new_dict_list


def sort_by_date(operations_dates_list: list, direction: bool = True) -> list:
    """Функцию возвращает новый список, отсртированный по дате, в начале последние операции"""

    # Сортировка списка
    new_operations_list = sorted(operations_dates_list, key=lambda x: x["date"], reverse=direction)

    return new_operations_list
