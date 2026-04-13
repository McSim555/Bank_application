import re
from collections import Counter


def process_bank_search(data_operations: list[dict], search_element: str) -> list[dict]:
    """Функцию возвращает список словарей, у которых в описании есть данная строка"""

    pattern = re.compile(search_element.lower())

    filtered_operations = []
    for operation in data_operations:
        if "description" in operation and pattern.search(operation["description"].lower()):
            filtered_operations.append(operation)

    return filtered_operations


def process_bank_operations(data_operations: list[dict], operations_categories: list) -> dict:
    """Функцию возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""

    categories_list = [operation["description"] for operation in data_operations if "description" in operation]

    operations_count = Counter(categories_list)

    filtered_operations_count = {}
    for key, value in operations_count.items():
        if key in operations_categories:
            filtered_operations_count[key] = value

    return filtered_operations_count
