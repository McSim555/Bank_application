from csv_excel_data_upload import csv_data_upload, excel_data_upload
from generators import filter_by_currency
from processing import filter_by_state, sort_by_date
from search_count_operations import process_bank_search
from utils import financial_transactions
from widget import get_date, mask_account_card


def main()->None:
    """Функция отвечает за основную логику проекта и связывает функциональности между собой"""

    # Выбор файла с банковскими транзакциями из директории data
    i = 0
    while i < 1:
        customer_choice = input(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n"
        )

        if customer_choice == "1":
            i += 1
            print("Для обработки выбран JSON-файл")
            operations_list = financial_transactions("../data/operations.json")
        elif customer_choice == "2":
            i += 1
            print("Для обработки выбран CSV-файл")
            operations_list = csv_data_upload("../data/transactions.csv")
        elif customer_choice == "3":
            i += 1
            print("Для обработки выбран Excel-файл")
            operations_list = excel_data_upload("../data/transactions_excel.xlsx")
        else:
            print("Некорректный ввод. Сделайте выбор, введя цифру 1 - 3")

    # Удаление пустых транзакций из списка операций
    for operation in operations_list:
        if operation == {}:
            operations_list.remove(operation)

    # Выбор статуса операции
    k = 0
    while k < 1:
        status_choice_customer = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        status_choice = status_choice_customer.upper()
        if status_choice == "EXECUTED" or status_choice == "CANCELED" or status_choice == "PENDING":
            k += 1
            operations_list = filter_by_state(operations_list, status_choice)
            print(f"Операции отфильтрованы по статусу [{status_choice}]")
        else:
            print(f"Статус операции {status_choice} недоступен.")

    # Сортировка по дате
    ii = 0
    while ii < 1:
        sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n")
        sort_by_date_up = sort_by_date_choice.upper()
        if sort_by_date_up == "ДА":
            ii += 1
            iii = 0
            while iii < 1:
                sorting_direction = input("Отсортировать по возрастанию даты или по убыванию?\n").lower()
                if sorting_direction == "по возрастанию":
                    iii += 1
                    operations_list = sort_by_date(operations_list)
                elif sorting_direction == "по убыванию":
                    iii += 1
                    operations_list = sort_by_date(operations_list, False)
                else:
                    print('Напишите "по возрастанию" или "убыванию"')
        elif sort_by_date_up == "НЕТ":
            ii += 1
            continue
        else:
            print(f'Вы написали {sort_by_date_choice}. Выберите "да" или "нет"')

    # Вывод рублевых транзакций или нет
    kk = 0
    while kk < 1:
        currency_output_choice = input("Выводить только рублевые транзакции? Да/Нет\n").upper()
        if currency_output_choice == "ДА":
            kk += 1
            operations_list = filter_by_currency(operations_list, "RUB")
        elif currency_output_choice == "НЕТ":
            kk += 1
            continue
        else:
            print(f'Вы написали {currency_output_choice}. Выберите "да" или "нет"')

    # Фильтрация по определенному слову в описании
    kkk = 0
    while kkk < 1:
        key_word_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").upper()
        if key_word_choice == "ДА":
            kkk += 1
            key_word = input(
                'Введите описание искомых транзакций, например, "Перевод с карты на карту", "Перевод со счета на счет", "Открытие вклада", ... \n'
            )
            operations_list = process_bank_search(operations_list, key_word)
        elif key_word_choice == "НЕТ":
            kkk += 1
            continue
        else:
            print(f'Вы написали {key_word_choice}. Выберите "да" или "нет"')

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(list(operations_list))}\n")

    if len(list(operations_list)) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    else:
        for operation in operations_list:
            if "from" in operation and operation["from"] != "":
                date = get_date(operation["date"])
                account_from = mask_account_card(operation["from"])
                account_to = mask_account_card(operation["to"])
                print(
                    f'{date} {operation["description"]}\n{account_from} -> {account_to}\nСумма: {operation["amount"]} {operation['currency_name']}\n'
                )

            else:
                date = get_date(operation["date"])
                account_to = mask_account_card(operation["to"])
                print(
                    f'{date} {operation["description"]}\n{account_to}\nСумма: {operation["amount"]} {operation['currency_name']}\n'
                )


main()
