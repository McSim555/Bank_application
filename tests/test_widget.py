import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(name_number, expected):
    assert mask_account_card(name_number) == expected


def test_mask_account_card_short():
    with pytest.raises(TypeError):
        mask_account_card("Счет2712345123451234")


def test_mask_account_card_empty():
    with pytest.raises(TypeError):
        mask_account_card("")


def test_mask_account_card_digital():
    with pytest.raises(TypeError):
        mask_account_card("123456789123456789123456")


def test_mask_account_card_mix():
    with pytest.raises(TypeError):
        mask_account_card("Visa 1Classic 6831982476737658")


def test_get_date_normal():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_mix():
    with pytest.raises(TypeError):
        get_date("202t-03-11T02:26:18.671407")


def test_get_date_empty():
    with pytest.raises(TypeError):
        get_date("")


def test_get_date_format_error1():
    with pytest.raises(TypeError):
        get_date("2025503-11T02:26:18.671407")
