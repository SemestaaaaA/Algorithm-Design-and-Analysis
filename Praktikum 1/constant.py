import time

arr =["Semesta", "Yamal", "Lewandowski", "Rafinha", "Franky", "Pedri"]

start_time = time.perf_counter()
first_value = arr[0]
print(f"Nilai Array[0]: {first_value}")
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Waktu Eksekusi: {execution_time:.10f} seconds")

