import time

def linear_time(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = list(range(1, 8))

start_time = time.perf_counter()
result = linear_time(arr)
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Hasil {arr}: {result}")
print(f"Waktu eksekusi: {execution_time:.10f} seconds")

