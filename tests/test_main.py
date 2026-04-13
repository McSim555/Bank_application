import unittest
from unittest.mock import patch

from src.main import main


class TestMainFunction(unittest.TestCase):

    @patch("src.main.sort_by_date")  # 4-й параметр метода
    @patch("src.main.filter_by_state")  # 3-й параметр метода
    @patch("builtins.input")  # 2-й параметр метода
    @patch("src.main.csv_data_upload")  # 1-й параметр метода
    def test_main_with_csv_and_filters(self, mock_csv_upload, mock_input, mock_filter_state, mock_sort_date):
        # Настройка моков
        mock_csv_upload.return_value = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]

        # filter_by_state должна вернуть те же данные (или отфильтрованные)
        mock_filter_state.return_value = mock_csv_upload.return_value

        # sort_by_date должна вернуть данные (можно те же)
        mock_sort_date.return_value = mock_csv_upload.return_value

        # Симуляция ввода пользователя:
        # '2' – выбор CSV-файла
        # 'EXECUTED' – фильтр по статусу
        # 'Да' – выполнить сортировку
        # 'по возрастанию' – сортировка по дате (ascending)
        # 'Нет' – не применять дополнительные фильтры
        # 'Нет' – завершить (или аналогично)
        mock_input.side_effect = ["2", "EXECUTED", "Да", "по возрастанию", "Нет", "Нет"]

        expected_result = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]
        # Вызов тестируемой функции
        result = main()
        assert result == expected_result

        # Дополнительно можно проверить, что моки были вызваны с правильными аргументами
        mock_csv_upload.assert_called_once()
        mock_filter_state.assert_called_once()
        mock_sort_date.assert_called_once()

    @patch("src.main.sort_by_date")  # 4-й параметр метода
    @patch("src.main.filter_by_state")  # 3-й параметр метода
    @patch("builtins.input")  # 2-й параметр метода
    @patch("src.main.excel_data_upload")  # 1-й параметр метода
    def test_main_with_excel_and_filters(self, mock_excel_upload, mock_input, mock_filter_state, mock_sort_date):
        # Настройка моков
        mock_excel_upload.return_value = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]

        # filter_by_state должна вернуть те же данные (или отфильтрованные)
        mock_filter_state.return_value = mock_excel_upload.return_value

        # sort_by_date должна вернуть данные (можно те же)
        mock_sort_date.return_value = mock_excel_upload.return_value

        # Симуляция ввода пользователя:
        # '3' – выбор Excel-файла
        # 'EXECUTED' – фильтр по статусу
        # 'Да' – выполнить сортировку
        # 'по возрастанию' – сортировка по дате (ascending)
        # 'Нет' – не применять дополнительные фильтры
        # 'Нет' – завершить (или аналогично)
        mock_input.side_effect = ["3", "EXECUTED", "Да", "по возрастанию", "Нет", "Нет"]

        expected_result = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]
        # Вызов тестируемой функции
        result = main()
        assert result == expected_result

        # Дополнительно можно проверить, что моки были вызваны с правильными аргументами
        mock_excel_upload.assert_called_once()
        mock_filter_state.assert_called_once()
        mock_sort_date.assert_called_once()

    @patch("src.main.sort_by_date")  # 4-й параметр метода
    @patch("src.main.filter_by_state")  # 3-й параметр метода
    @patch("builtins.input")  # 2-й параметр метода
    @patch("src.main.financial_transactions")  # 1-й параметр метода
    def test_main_with_json_and_filters(self, mock_json_upload, mock_input, mock_filter_state, mock_sort_date):
        # Настройка моков
        mock_json_upload.return_value = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]

        # filter_by_state должна вернуть те же данные (или отфильтрованные)
        mock_filter_state.return_value = mock_json_upload.return_value

        # sort_by_date должна вернуть данные (можно те же)
        mock_sort_date.return_value = mock_json_upload.return_value

        # Симуляция ввода пользователя:
        # '1' – выбор JSON-файла
        # 'EXECUTED' – фильтр по статусу
        # 'Да' – выполнить сортировку
        # 'по возрастанию' – сортировка по дате (ascending)
        # 'Нет' – не применять дополнительные фильтры
        # 'Нет' – не искать по слову
        mock_input.side_effect = ["1", "EXECUTED", "Да", "по возрастанию", "Нет", "Нет"]

        expected_result = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]
        # Вызов тестируемой функции
        result = main()
        assert result == expected_result

    @patch("src.main.process_bank_search")  # 6-й параметр метода
    @patch("src.main.filter_by_currency")  # 5-й параметр метода
    @patch("src.main.sort_by_date")  # 4-й параметр метода
    @patch("src.main.filter_by_state")  # 3-й параметр метода
    @patch("builtins.input")  # 2-й параметр метода
    @patch("src.main.financial_transactions")  # 1-й параметр метода
    def test_main_with_json_and_max_number_filters(
        self, mock_json_upload, mock_input, mock_filter_state, mock_sort_date, mock_currency, mock_bank_search
    ):
        # Настройка моков
        mock_json_upload.return_value = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]

        # filter_by_state должна вернуть те же данные (или отфильтрованные)
        mock_filter_state.return_value = mock_json_upload.return_value

        mock_sort_date.return_value = mock_json_upload.return_value

        mock_currency.return_value = mock_json_upload.return_value

        mock_bank_search.return_value = mock_json_upload.return_value

        # Симуляция ввода пользователя:
        # '1' – выбор JSON-файла
        # 'EXECUTED' – фильтр по статусу
        # 'Да' – выполнить сортировку
        # 'по возрастанию' – сортировка по дате (ascending)
        # 'Да' – не применять дополнительные фильтры
        # 'Да' - выполнить поиск
        # 'счет' - ключевое слово
        mock_input.side_effect = ["1", "EXECUTED", "Да", "по возрастанию", "Да", "Да", "счет"]

        expected_result = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-01-01T12:00:00",
                "description": "Test",
                "from": "Card 1234123412341234",
                "to": "Счет 56781234123412341234",
                "amount": 100,
                "currency_name": "RUB",
            }
        ]
        # Вызов тестируемой функции
        result = main()
        assert result == expected_result
