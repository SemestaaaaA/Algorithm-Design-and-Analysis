def rekursif_factorial(nilai):
    if nilai == 1:
        return nilai
    else:
        return nilai * rekursif_factorial(nilai - 1)
    
def iterasi_faktorial(nilai):
    hasil = 1
    for i in range(nilai):
        hasil = hasil * (i + 1)
    return hasil

# Meminta input dari pengguna
nilai = int(input("Masukkan nilai faktorial yang ingin dihitung: "))
print(f"Hasil perhitungan dari {nilai}! adalah sebagai berikut:")
print(f"Rekursif = {rekursif_factorial(nilai)}")
print(f"Iterasi = {iterasi_faktorial(nilai)}")
