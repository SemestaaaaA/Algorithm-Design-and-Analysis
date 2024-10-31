import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 5

start_time = time.perf_counter()
result = factorial(n)
end_time = time.perf_counter()

print(f"Hasil {n}! adalah = {result}")
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.10f} seconds")

