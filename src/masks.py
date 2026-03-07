def get_mask_card_number(card_number: str) -> str:
    """Функция принмает нв вход номер карты и возвращает маску."""

    mask_card_number = ""
    if card_number.isdigit():
        if len(card_number) == 16:
            mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        elif len(card_number):
            raise ValueError("Номер карты должен состоять из 16 цифр")
    else:
        raise TypeError("Номер карты должен состоять из 16 цифр")
    return mask_card_number



# def get_mask_account(account_number: int) -> str:
#     """Функция принимает на вход номер счета и возвращает его маску"""
#     str_account_number = str(account_number)  # Первод номера счета в строку
#     mask_account_number = "**" + str_account_number[-4:]
#     return mask_account_number
#
# print(get_mask_card_number(1.1))