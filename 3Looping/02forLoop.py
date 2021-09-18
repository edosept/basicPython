# contoh 1
print("Contoh 1 : ")
data1 = range(5)
print(data1, type(data1))

listData1 = list(data1)
print(listData1, type(listData1), "\n")

# contoh 2
print("Contoh 2 : ")
data2 = range(5, 9)
print(data2, type(data2))

listData2 = list(data2)
print(listData2, type(listData2), "\n")

# contoh 3
print("Contoh 3 : ")
data3 = range(7, 3)
print(data3, type(data3))

listData3 = list(data3)
print(listData3, type(listData3), "\n")

# contoh 4
print("Contoh 4 : ")
data4 = range(7, 3, -1)
print(data4, type(data4))

listData4 = list(data4)
print(listData4, type(listData4), "\n")

# contoh 5
print("Contoh 5 : ")
data5 = range(2, 14, 3)
print(data5, type(data5))

listData5 = list(data5)
print(listData5, type(listData5), "\n")

print("=" * 50)
# for itu untuk menampilkan apa yang ada di in, in ini bisa range, bisa variabel, dll
# atau si for itu jg bisa digunakan lebih lanjut misal digunakan dalam list.
# ya pokoknya si for ini outputnya dri loop yang kita ambil dari --> in
# contoh 1
for angka in range(5):
    print(angka)

# contoh 2
for angka in range(10, 1, -3):
    print('angka = {}'.format(angka))

# contoh 3
for char in "Hello guys!":
    print("char = ", char)
