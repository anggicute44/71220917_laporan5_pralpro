def cek_angka(a, b, c):
    if a == b or a == c or b == c:
        return False

    if a + b == c or a + c == b or b + c == a:
        return True

    return False
