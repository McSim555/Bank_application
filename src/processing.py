def filter_by_state(operations_list_1: list, target_state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список по ключу state"""

    new_operations_list = list()
    for operation in operations_list_1:
        if "state" in operation:
            if operation["state"] == target_state:
                # Новый список словарей по ключу
                new_operations_list.append(operation)
            else:
                continue
        else:
            raise KeyError("Как минимум в одном из входных словарей ключа state нет")

    return new_operations_list


def sort_by_date(operation_dates: list, direction: bool = True) -> list:
    """Функцию возвращает новый список, отсортированный по дате, в начале последние операции"""

    new_operations_dates = list()
    for operation in operation_dates:
        if "date" in operation:
            if operation["date"] != "":
                # Сортировка списка
                new_operations_dates.append(operation)
            else:
                raise ValueError("Отсутствует дата в одной или нескольких операциях")
        else:
            raise KeyError("В одной или нескольких операциях отсутствует дата")

    # Сортировка списка
    new_operations_dates_final = sorted(new_operations_dates, key=lambda x: x["date"], reverse=direction)

    return new_operations_dates_final
