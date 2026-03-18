import time

def log(filename=''):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time.ctime(int(time.time()))
                result = func(*args, **kwargs)
                end_time = time.ctime(int(time.time()))
                if filename == '':
                    print(f'{func} result OK: {result}')
                elif filename == 'mylog.txt':
                    with open(filename, 'a') as file:
                        file.write(f'\n{func} result OK: {result}')
                else:
                    raise ValueError('Имя файла указано неверно')
            except Exception as e:
                if filename == '':
                    print(f'{func} error: ({e}). Inputs {args}, {kwargs} ')
                elif filename == 'mylog.txt':
                    with open(filename, 'a') as file:
                        file.write(f'\n{func} error: ({e}). Inputs {args}, {kwargs} ')
                else:
                    raise ValueError('Имя файла указано неверно')
        return wrapper
    return my_decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x/y

my_function(4, 1)
