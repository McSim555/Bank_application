def filter_by_state(operations_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    for operation in operations_list:
        if 'state' in operation:
            # Новый список словарей по ключу
            new_operations_list = [operations for operations in operations_list if operations["state"] == state]
            return new_operations_list
        else:
            raise KeyError("Как минимум в одном из входных словарей ключа state нет")


def sort_by_date(operation_dates: list, direction: bool = True) -> list:
    """Функцию возвращает новый список, отсртированный по дате, в начале последние операции"""

    for operation in operation_dates:
        if 'date' in operation:
            if operation['date'] != "":
                # Сортировка списка
                new_operations_dates = sorted(operation_dates, key=lambda x: x["date"], reverse=direction)
                return new_operations_dates
            else:
                raise ValueError("Отсутствует дата в одной или нескольких операциях")
        else:
            raise KeyError("В одной или нескольких операциях отсутсвует дата")
