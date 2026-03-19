import pytest

from src.decorators import log


def test_log_consol(capsys):
    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(4, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function result OK: 5\n"


def test_log_txtfile():
    @log(filename="test_mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(4, 1)
    with open("test_mylog.txt", "r") as file:
        content = file.read()
        assert content == "\nmy_function result OK: 5"
    with open("test_mylog.txt", "w") as file:
        file.write("")


def test_log_wrong_file_name():
    @log(filename="test")
    def my_function(x, y):
        return x + y

    with pytest.raises(ValueError):
        my_function(4, 1)


def test_log_error_consol(capsys):
    @log(filename="")
    def my_function(x, y):
        return x / y

    my_function(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: (division by zero). Inputs (4, 0), {}\n"


def test_log_error_txtfile():
    @log(filename="test_mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(4, 0)
    with open("test_mylog.txt", "r") as file:
        content = file.read()
        assert content == "\nmy_function error: (division by zero). Inputs (4, 0), {}"
    with open("test_mylog.txt", "w") as file:
        file.write("")


def test_log_error_wrong_file_name():
    @log(filename="test")
    def my_function(x, y):
        return x / y

    with pytest.raises(ValueError):
        my_function(4, 0)
