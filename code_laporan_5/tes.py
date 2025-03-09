# def tampilkan_ulang_tahun(tanggal_lahir):
#     print("Tanggal lahir Anda", tanggal_lahir, "selamat ultah!")

# # Meminta input dari pengguna
# data = input("Masukkan tanggal lahir: ")

# # Memanggil fungsi dengan argumen
# tampilkan_ulang_tahun(data)


# def Fungsi(nama):
#     pesan = "Halo, " + nama + "! Selamat datang!"  # Membuat pesan 
#     return pesan  

# # memmanggi  fungsi yaitu nama
# hasil_sapaan = Fungsi("Rani")
# print(hasil_sapaan)

# def kuadrat(x):
#     return x * x
# result = kuadrat(9) # result akan bernilai 81
# print(result)

# def pembagian(a, b):
#     if b == 0:
#         return None  # Langsung keluar jika pembagi adalah 0
#     return a / b


# hasil = pembagian(10, 2)
# print(hasil)  





# def bagi(x, y):
#     return x/y, x%y
# hasil_bagi, sisa = bagi(10, 2)
# print(hasil_bagi) # hasil_bagi akan bernilai 5

# def statistik(angka):
#     total = 0
#     for n in angka:
#         total += n

#     mean = total / len(angka)  # Menghitung rata-rata
#     return total, mean  # Mengembalikan dua nilai sekaligus

# # Contoh penggunaan
# data = [10, 20, 30, 40, 50]
# total, rata_rata = statistik(data)


# def fungsi(x, y=10):
#     return x + y

# #  fungsi dengan satu argumen di panggil, y akan menggunakan nilai default 10
# hasil1 = fungsi(5)
# print("Hasil 1:", hasil1)  # Output: 15 (karena 5 + 10)

# # fungsi dengan dua argumen dipanggil, y akan menggunakan nilai 15
# hasil2 = fungsi(5, 15)
# print("Hasil 2:", hasil2)  # Output: 20 (karena 5 + 15)


# def fungsi(x, y):
#     return x + y
# # Memanggil fungsi dengan keyword arguments
# hasil = fungsi(x=5, y=10)
# print("Hasil:", hasil)  # Output 15 

# Fungsi biasa
# def pangkat(a):
#     return a** 2
# pangkat_lambda = lambda a: a ** 2 #lambda a: a ** 2 untuk menggantikan fungsi pangkat(a).
# print(pangkat_lambda(5))  # Output: 25


tambah = lambda a, b: a + b
# Fungsi lambda a, b: a + b disimpan dalam variabel tambah
print(tambah(3, 7))  # Output: 10


#lambda x: x ** 2 digunakan langsung dalam map().
angka = [1, 2, 3, 4]
kuadrat = list(map(lambda x: x ** 2, angka))
print(kuadrat)  # Output: [1, 4, 9, 16]


