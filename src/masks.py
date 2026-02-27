def get_mask_card_number(card_number: int) -> str:
    """Функция принмае нв вход номер карты и возвращает маску."""
    str_card_number = str(card_number)  # Перевод номера карты в строку
    mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    str_account_number = str(account_number)  # Первод номера счета в строку
    mask_account_number = "**" + str_account_number[-4:]
    return mask_account_number
