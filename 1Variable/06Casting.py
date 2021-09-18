# casting --> perubahan tipe data sesuai kebutuhan, misal yg awalnya int mau dirubah ke str

# membuat variable a dan isinya integer 20
a = 20
print("data dan tipe data variable a pertama kali")
print(a, type(a))

# ubah tipe data variable a jadi string
a = str(a)
print("data dan tipe data variable a menjadi string")
print(a, type(a))

# ubah tipe data variable a jadi float
a = float(a)
print("data dan tipe data variable a menjadi float")
print(a, type(a))

# tipe data variable a tidak berubah
int(a)
print("data dan tipe data variable a tetap float, karena a belum disimpan ke variable a")
print(a, type(a))

# ubah tipe data variable a jadi int kembali
a = int(a)
print("data dan tipe data variable a menjadi int")
print(a, type(a))

# data pada variable a tetap int
# tetapi yang muncul menggunakan format float
print("data dan tipe data variable a tetap int, tapi yang muncul float")
print(float(a), type(float(a)))
print("karena disini si casting float langsung tampil dengan fungsi print")
print("pembuktian klo si a masih int karena variable a kita sebelumnya masih int")
print(a, type(a))