def contoh1(list, x):
    for angka in list:
        if angka == x:
            return True
    return False

my_list = [1, 2, 3, 4, 5]
x = 10

if contoh1(my_list, x):
    print(f"{x} ditemukan dalam daftar.")
else:
    print(f"{x} tidak ditemukan dalam daftar.")
