import logging
import os

os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
)

masks_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает нв вход номер карты и возвращает маску."""

    masks_logger.info(f"Введен номер карты: {card_number}")
    error_message = "Номер карты должен состоять из 16 цифр"
    if card_number.isdigit():
        if len(card_number) == 16:
            mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
            masks_logger.info(f"Сформирована маска номера карты: {mask_card_number}")
            return mask_card_number
        else:
            masks_logger.error(error_message)
            raise ValueError(error_message)
    else:
        masks_logger.error(error_message)
        raise TypeError(error_message)


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    masks_logger.info(f"Введен номер счета: {account_number}")
    error_message = "Номер счета должен состоять из 20 цифр"
    # int(account_number)
    if account_number.isdigit():
        if len(account_number) == 20:
            mask_account_number = "**" + account_number[-4:]
            masks_logger.info(f"Сформирована маска счета: {mask_account_number}")
            return mask_account_number
        else:
            masks_logger.error(error_message)
            raise ValueError(error_message)
    else:
        masks_logger.error(error_message)
        raise TypeError(error_message)
