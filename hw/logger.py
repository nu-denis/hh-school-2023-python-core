import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Метод {func.__name__} начался в {start_time} секунд, завершился в {end_time} секунд. Общее время выполнения: {total_time} секунд.")
        return result
    return wrapper
