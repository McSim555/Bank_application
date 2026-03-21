import os


def log(filename=""):  # При выводе в файл указать имя файла в формате .txt
    """Декоратор выводит в консоль или записывает в файл .txt логи работы функции"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename == "":
                    print(f"{func.__name__} ok")
                elif os.path.splitext(filename)[1] == ".txt":
                    with open(filename, "a") as file:
                        file.write(f"\n{func.__name__} ok")
                else:
                    raise ValueError("Имя файла указано неверно")
                return result
            except Exception as e:
                if filename == "":
                    print(f"{func.__name__} error: ({e}). Inputs {args}, {kwargs}")
                elif os.path.splitext(filename)[1] == ".txt":
                    with open(filename, "a") as file:
                        file.write(f"\n{func.__name__} error: ({e}). Inputs {args}, {kwargs}")
                else:
                    raise ValueError("Имя файла указано неверно")
                raise

        return wrapper

    return my_decorator
