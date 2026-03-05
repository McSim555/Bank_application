def filter_by_state(operations_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    # Новый список словарей по ключу
    new_operations_list = [operations for operations in operations_list if operations["state"] == state]
    return new_operations_list


def sort_by_date(operation_dates: list, direction: bool = True) -> list:
    """Функцию возвращает новый список, отсртированный по дате, в начале последние операции"""

    # Сортировка списка
    new_operations_dates = sorted(operation_dates, key=lambda x: x["date"], reverse=direction)
    return new_operations_dates
