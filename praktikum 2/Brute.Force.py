text = 'Python adalah bahasa pemrograman yang digunakan untuk membuat aplikasi, situs web, perangkat lunak, dan melakukan analisis data. Python merupakan bahasa pemrograman yang populer dan banyak digunakan karena mudah dipelajari, efisien, dan dapat dijalankan di berbagai platform. Python memiliki sintaksis yang sederhana dan mudah dipahami. Pemformatannya tidak berantakan secara visual, dan sering kali menggunakan kata kunci bahasa Inggris. Python bersifat open source sehingga dapat diunduh dan dipasang secara gratis. Python dapat digunakan untuk berbagai keperluan, seperti ilmu data, pengembangan web, serta pembelajaran mesin.'

katakunci = 'Python'

def search(text, katakunci):
    lt = len(text)
    lp = len(katakunci)
    jumlahhasil = 0

    for i in range(lt - lp + 1):
        ditemukan = True
        for j in range(lp):
            if text[i + j] != katakunci[j]:
                ditemukan = False
                break
        if ditemukan:
            jumlahhasil += 1

    return jumlahhasil

# Menjalankan fungsi
totalhasil = search(text, katakunci)
print("======= Pencarian menggunakan algoritma bruteforce ======")
print(f"kalimat/text : \n{text}\n")
print(f"kata yang akan dicari/pattern : {katakunci}\n")
print(f"total jumlah kata \"{katakunci}\" dalam text sebanyak : {totalhasil}")

