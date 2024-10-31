import time

def quadratic_time(arr):
    pairs = []
    for i in arr:
        for j in arr:
            pairs.append((i, j))
    return pairs

arr = list(range(1, 4))

start_time = time.perf_counter()
result = quadratic_time(arr)
end_time = time.perf_counter()

print(f"Hasil Perhitungan: {arr} Panjang {len(result)}")
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.10f} seconds")