import time

# Лабораторна робота 23. Завдання 1. Коритко Артур


def trace(func):
    def wrapper(*args, **kwargs):
        print(
            f"Вызов {func.__name__} потом аргс- {args}, ну и кваргдс - {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} возвращаем {result}")
        return result
    return wrapper


@trace
def add(a, b):
    return a + b


add(2, 3)

# Лабораторна робота 23. Завдання 2. Коритко Артур


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {
              end_time - start_time} секунд")
        return result
    return wrapper


@measure_time
def example_function():
    time.sleep(2)


example_function()


# Лабораторна робота 23. Завдання 3. Коритко Артур

def require_user_role(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                raise PermissionError(f"Доступ запрещен. Нужна роль: {role}.")
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator


@require_user_role("admin")
def access_admin_panel(user_role):
    print("Вы вошли в панель Администратора. Добро пожаловать")


access_admin_panel("admin")
