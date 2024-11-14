def contoh2(list, target):
    n = len(list)
    for i in range(n):
        for j in range(i + 1, n):
            if list[i] + list[j] == target:
                return (list[i], list[j])
    return None  # Mengembalikan None jika tidak ada pasangan yang ditemukan

# Contoh penggunaan
daftar_angka = [1, 3, 5, 7, 9]
target = 9
result = contoh2(daftar_angka, target)

if result:
    print(f"Pasangan yang jumlahnya {target} adalah: {result}")
else:
    print(f"Tidak ada pasangan yang jumlahnya {target}")
