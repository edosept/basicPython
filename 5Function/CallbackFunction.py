# Callback Function
'''
Callback Function adalah sebutan untuk sebuah function yang menjadi argument bagi function lainnya
'''


def tambah(num1, num2):
    return num1 + num2


def kurang(num1, num2):
    return num1 - num2


def hitung(fnOperator, angka1, angka2):
    hasil = fnOperator(angka1, angka2)
    return hasil


print(hitung(tambah, 9, 5))
print(hitung(kurang, 9, 5))

print("=" * 50)
# Calling other Function
'''
Selain dengan menggunakan metode callback function,
didalam suatu function kita juga dapat memanggil function lain dengan memanggil nama functionnya.
'''


def tampilkanJawaban(jawaban):
    print('Jawaban = {}'.format(jawaban))
# klo ada perubahan kata kata di dalam print,
# kedepannya kita hanya ubah disini

# karena disini kita sudah panggil di masing masing function


def pertambahan(angka1, angka2):
    hasil = angka1 + angka2
    tampilkanJawaban(hasil)  # memanggil function tampilkanJawaban


def pengurangan(angka1, angka2):
    hasil = angka1 - angka2
    tampilkanJawaban(hasil)


def perkalian(angka1, angka2):
    hasil = angka1 * angka2
    tampilkanJawaban(hasil)


def pembagian(angka1, angka2):
    hasil = angka1 / angka2
    tampilkanJawaban(hasil)


pertambahan(10, 5)
pengurangan(10, 5)
perkalian(10, 5)
pembagian(10, 5)
