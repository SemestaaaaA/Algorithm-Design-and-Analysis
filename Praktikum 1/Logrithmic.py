import time

def pow(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        num = pow(x, n//2)
        return num * num
    
    return x * pow(x, n - 1)
start_time = time.perf_counter()

print(pow(2, 3))
print(pow(5, 3))
print(pow(10, 2))

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Waktu Eksekusi:  {execution_time:.10f} seconds") 

