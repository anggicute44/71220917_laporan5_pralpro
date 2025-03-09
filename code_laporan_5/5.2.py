def cek_digit_belakang():
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    a_digit = a % 10
    b_digit = b % 10
    c_digit = c % 10
    if a_digit == b_digit or a_digit == c_digit or b_digit == c_digit:
        print(True)
    else:
        print(False)
cek_digit_belakang()
print(30, 20, 18)

cek_digit_belakang()
print(145, 5, 100)

cek_digit_belakang()
print(71, 187, 18)

cek_digit_belakang()
print(1024, 14, 94)

cek_digit_belakang()
print(53, 8900, 658)
