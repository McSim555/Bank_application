import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_full(test_card_number_full):
    assert get_mask_card_number(test_card_number_full) == "7365 41** **** 3587"


def test_get_mask_card_number_short(test_number_short):
    with pytest.raises(ValueError):
        get_mask_card_number(test_number_short)


def test_get_mask_card_number_empty(test_number_empty):
    with pytest.raises(TypeError):
        get_mask_card_number(test_number_empty)


def test_get_mask_card_number_letters(test_number_letters):
    with pytest.raises(TypeError):
        get_mask_card_number(test_number_letters)


@pytest.mark.parametrize(
    "test_case, expected", [("73654108430135874305", "**4305"), ("12341234123412341234", "**1234")]
)
def test_get_mask_account(test_case, expected):
    assert get_mask_account(test_case) == expected


def test_get_mask_account_short(test_number_short):
    with pytest.raises(ValueError):
        get_mask_account(test_number_short)


def test_get_mask_account_empty(test_number_empty):
    with pytest.raises(TypeError):
        get_mask_account(test_number_empty)


def test_get_mask_account_letters(test_number_letters):
    with pytest.raises(TypeError):
        get_mask_card_number(test_number_letters)
