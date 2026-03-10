from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Функция принимает название и номер карты или номер счета и возвращает в замаскированном виде"""

    if "Счет" in card_or_account_number:  # Проверка введен счет или карта
        if card_or_account_number[4] == " ":
            # Формирование замаскированного вывода для счета:
            masked_account = "Счет " + get_mask_account(card_or_account_number[5:])
            return masked_account
        else:
            raise TypeError("Некорректный ввод")
    else:
        if card_or_account_number[-16:].isdigit():
            if card_or_account_number[-17] == " ":
                if any(character.isdigit() for character in card_or_account_number[0:-18]):
                    raise TypeError("Некорректный ввод")
                else:
                    # Формирование замаскированного вывода для карты:
                    masked_card = card_or_account_number[:-16] + get_mask_card_number(card_or_account_number[-16:])
                    return masked_card
            else:
                raise TypeError("Некорректный ввод")
        else:
            raise TypeError("Некорректный ввод")


def get_date(input_date: str) -> str:
    """Функция принимает набор данных, содержащих дату, и возвращает только дату в заданном формате"""
    if (
        input_date[0:4].isdigit()
        and input_date[4] == "-"
        and input_date[5:7].isdigit()
        and input_date[4] == "-"
        and input_date[8:10].isdigit()
    ):
        cleaned_date = input_date[:10]  # Отрезаем лишнее
        date_list = cleaned_date.split("-")  # Разбиваем строку на три элемента: год, месяц, день
        target_date = date_list[2] + "." + date_list[1] + "." + date_list[0]  # Сборка даты в заданном формате
        return target_date
    else:
        raise TypeError("Некорректный формат ввода даты")
