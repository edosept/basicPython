'''
Local Variable didefinisikan sebagai jenis variable yang dideklarasikan dalam suatu blok pemrograman.
Local Variable hanya dapat digunakan di dalam blok kode dimana dia dideklarasikan/dibuat.

Global Variable adalah variable yang didefinisikan di luar function,
global variable memiliki cakupan global yang brarti memegang nilainya sepanjang masa program dijalankan.
oleh karena itu dapat diakses di seluruh program oleh function apapun yang terdapat di dalam program.
'''


def coba():
    print(x + 2)  # smua yg di dalam function coba ini adalah local
    return x + 3


x = 5  # Global
print(coba(), x)  # variable x nya ambil dari global
# 7
# 8 5


def cobaLagi():
    x = 8  # Local Variable
    print(x + 2)  # smua yg di dalam function coba ini adalah local
    return x + 3


x = 5  # Global
print(cobaLagi(), x)  # variable x nya ambil dari local
# 10
# 11 5


def cobaBisaJuga():
    global x  # variable x global dinyatakan di local
    x += 8  # maka kita disini akan menggunakan variable x global
    print(x + 2)
    return x + 3


x = 5  # Global
print(cobaBisaJuga(), x)
# 15
# 16 13
