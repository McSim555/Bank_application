def get_mask_card_number(card_number: str) -> str:
    """Функция принмает нв вход номер карты и возвращает маску."""

    error_message = "Номер карты должен состоять из 16 цифр"
    if card_number.isdigit():
        if len(card_number) == 16:
            mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
            return mask_card_number
        else:
            raise ValueError(error_message)
    else:
        raise TypeError(error_message)


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    error_message = "Номер счета должен состоять из 20 цифр"
    if account_number.isdigit():
        if len(account_number) == 20:
            mask_account_number = "**" + account_number[-4:]
            return mask_account_number
        else:
            raise ValueError(error_message)
    else:
        raise TypeError(error_message)

#print(get_mask_account("1234123412341234123"))