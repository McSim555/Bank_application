import pytest


@pytest.fixture
def test_card_number_full():
    return "7365410843013587"


@pytest.fixture
def test_card_number_short():
    return "736541084301358"

@pytest.fixture
def test_card_number_empty():
    return ""

@pytest.fixture
def test_card_number_letters():
    return "rterretrertyerty"


