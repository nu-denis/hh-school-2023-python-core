import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {round((end_time - start_time) * 1000, 3)} ms")
        return result

    return wrapper
