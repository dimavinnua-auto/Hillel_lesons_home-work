def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        print("-" * 30)
        return result
    return wrapper

# Використання:
@log_args_and_result
def add(a, b):
    return a + b

@log_args_and_result
def greet(name, greeting="Привіт"):
    return f"{greeting}, {name}!"

# Тестуємо:
add(3, 5)
greet("Олексій")
greet("Марія", greeting="Добрий вечір")




def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ZeroDivisionError as e:
            print(f"Помилка: ділення на нуль — {e}")
        except TypeError as e:
            print(f"Помилка: неправильний тип даних — {e}")
        except ValueError as e:
            print(f"Помилка: неправильне значення — {e}")
        except Exception as e:
            print(f"Невідома помилка: {type(e).__name__} — {e}")
    return wrapper


@handle_exceptions
def divide(a, b):
    return a / b

@handle_exceptions
def get_element(lst, index):
    return lst[index]


divide(10, 2)
divide(10, 0)
divide("a", 2)
get_element([1, 2, 3], 5)


