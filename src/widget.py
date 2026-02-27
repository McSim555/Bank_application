def mask_account_card(card_or_account_number: str) -> str:
    """Функция принимает название и номер карты или номер счета и возвращает в замаскированном виде"""
    import masks


    if 'Счет' in card_or_account_number:
        masked_account = 'Счет ' + masks.get_mask_account(int(card_or_account_number[5:]))
        return masked_account
    else:
        masked_card = card_or_account_number[:-16] + masks.get_mask_card_number(int(card_or_account_number[-16:]))
        return masked_card


