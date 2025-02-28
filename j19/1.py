import time
import numpy as np
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.10f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    sums = 0
    for _ in range(1, 1_000_001):
        sums += _
    print(sums)

slow_function()
# Output:
# Function executed
# slow_function ran in 2.00 seconds