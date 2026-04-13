from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_excel_data_upload import csv_data_upload, excel_data_upload  # замените на реальный импорт


@patch("builtins.open", new_callable=mock_open, read_data="id;amount;comment\n1;100;test\n2;200;another")
def test_csv_data_upload_success(mock_file):
    """Проверяем, что функция правильно читает мок-данные CSV"""
    result = csv_data_upload("fake_path.csv")

    expected = [{"id": "1", "amount": "100", "comment": "test"}, {"id": "2", "amount": "200", "comment": "another"}]
    assert result == expected

    # Проверяем, что open был вызван с правильными аргументами
    mock_file.assert_called_once_with("fake_path.csv", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_csv_data_upload_empty_file(mock_file):
    """Проверяем, что функция правильно читает мок-данные CSV"""
    result = csv_data_upload("fake_path.csv")

    expected = []
    assert result == expected


def test_csv_data_upload_no_file():
    """Проверяем, что функция правильно обрабатывает случай отсутствия файла"""

    result = csv_data_upload("fake_path.csv")
    expected = []
    assert result == expected


@patch("pandas.read_excel")
def test_excel_data_upload_success(mock_read_excel):
    """Тест нормальной обработки Excel файла"""
    mock_read_excel.return_value = pd.DataFrame(
        {"id": [1, 2], "amount": [100, 200], "comment": ["test", "another"], "from": ["M 1", ""]}
    )
    result = excel_data_upload("fake_path.xlsx")
    expected = [
        {"id": 1, "amount": 100, "comment": "test", "from": "M 1"},
        {"id": 2, "amount": 200, "comment": "another", "from": ""},
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_excel_data_empty_file(mock_read_excel):
    """Тест пустого Excel файла"""
    mock_read_excel.return_value = pd.DataFrame({})
    result = excel_data_upload("fake_path.xlsx")
    expected = []
    assert result == expected


def test_excel_data_no_file():
    """Тест отсутствия Excel файла"""

    result = excel_data_upload("fake_path.xlsx")
    expected = []
    assert result == expected
