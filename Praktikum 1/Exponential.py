import time

def fibbonaci_exponential(n):
    if n <= 1:
        return n
    return fibbonaci_exponential(n - 1) + fibbonaci_exponential(n - 2)

n = 12

start_time = time.perf_counter()
result = fibbonaci_exponential(n)
end_time = time.perf_counter()

print(f"Hasil fib({n}) : {result}")
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.10f} seconds")

