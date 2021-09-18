'''
List adalah sebuah tipe data yang dapat menyimpan data lebih dari satu.
List memiliki index, serta dapat menyimpan berbagai jenis data,
kita dapat menyimpan string, integer, boolean, dan tipe data lainnya secara bersamaan,
bahkan list juga bisa menyimpan list lain di dalamnya.

sifat list bisa menyimpan data yang sama atau duplikat

mengakses list by index dimulai dari nol
negative indexing dimulai dari -1, akses data paling belakang disebelah kanan, kebalikan dari index biasa
akses data jg bisa by range index
'''

# akses data
listContoh = ['hello', 1, 1, 3, True]

print(listContoh, type(listContoh))

print(listContoh[0])  # hello
print(listContoh[2])  # 1
print(listContoh[4])  # True

print(listContoh[-1])  # True
print(listContoh[-2])  # 3
print(listContoh[-5])  # hello

print(listContoh[-4:-1])  # [1, 1, 3]
print(listContoh[1:4])  # [1, 1, 3]
print(listContoh[-5:2])  # ['hello', 1]
print(listContoh[0:-2])  # ['hello', 1, 1]
print(listContoh[2:])  # [1, 3, True]

print("=" * 50)
# change data
print("change data")
listContoh = ['hello', 1, 1, 3, True]

listContoh[1] = "test"
listContoh[-2] = "coba"
print(listContoh)

print("=" * 50)
# add data
print("add data")
listContoh = ['hello', 1, 1, 3, True]

# append menambahkan item barunya pada index terakhir atau paling belakang
listContoh.append('coba')
# insert menambahkan item barunya sesuai index yang kita mau
listContoh.insert(1, 'boleh')
print(listContoh)

print("=" * 50)
# remove data
print("remove data")
listContoh = ['hello', 'coba', 'coba', 3, True]
# remove hanya bisa menghapus satu data saja pada list dan menghapus data yang pertama ditemukan saja
listContoh.remove('coba')
# pop kita tidak perlu memberikan argumen apapun dan pop mengahapus item terakhir pada suatu list
listContoh.pop()
# del itu remove item sesuai index yang kita mau
del listContoh[1]
print(listContoh)

# clear kita tidak perlu memberikan argumen apapun dan clear untuk menghapus seluruh item pada list
listContoh.clear()
print(listContoh)

print("=" * 50)
# loop in list
print("loop in list")
listContoh = ['hello', 1, 1, 3, True]

for item in listContoh:
    print(item)

print("=" * 50)
# check in list
print("check in list")
listContoh = ['hello', 1, 1, 3, True]

# cara1 check
check = 2 in listContoh
print(check)

# cara2 check
if "hello" in listContoh:
    print("Data ditemukan :)")
else:
    print("Data tidak ditemukan!")

print("=" * 50)
# length of list
listContoh = ['hello', 1, 1, 3, True]
print("length of list " + str(len(listContoh)))

print("=" * 50)
# method copy
# semua isi list dari variable lama akan di copy dan disimpan ke variable baru
# tujuannya sih biar gga ganggu list yang lama,
# klo ga dicopy jadi ngeganngu list lama jadi ada item yang ke replace
print("method copy")
listContoh = ['hello', 'coba', 'coba', 3, True]

newList1 = listContoh
newList1[1] = 'test'

newList2 = listContoh.copy()
newList2[2] = 'baru'

print(listContoh)
print(newList1)
print(newList2)

print("=" * 50)
# list concatenate
print("list concatenate")
listContoh = ['hello', 'coba', 'coba', 3, True]
listBaru = [5, "test", False]
listCoba = ["tarik", 8]

listGabungan = listBaru + listContoh
print(listGabungan)

# extend nih sama aja concatenate kaya si plus (+)
listGabungan.extend(listCoba)
print(listGabungan)

print("=" * 50)
# find index
print("find index")
listContoh = ["eddie", "edo", "andi", "charlie", "samson"]
findIndex = listContoh.index('edo')

print(findIndex, type(findIndex))

print("=" * 50)
# sorting
print("sorting")
listContoh = ["eddie", "edo", "andi", "charlie", "samson"]
listContoh.sort()

print(listContoh)  # ['andi', 'charlie', 'eddie', 'edo', 'samson']

listAngka = [4, 3, 1, 5, 2]
# pengurutannya jadi desc, dimana dari terbesar sampai terkecil
listAngka.sort(reverse=True)

print(listAngka)  # [5, 4, 3, 2, 1]

print("=" * 50)
# reverse
print("reverse")
# method reverse tidak mengurutkan data layaknya method sort,
# reverse hanya membalikkan urutan data
listContoh = ["eddie", "edo", "andi", "charlie", "samson"]
listContoh.reverse()

print(listContoh)  # ['samson', 'charlie', 'andi', 'edo', 'eddie']

print("=" * 50)
# list dua dimensi
things = [
    ['red pen', 'blue pen'],
    ['analog clock', 'digital clock'],
    ['futsal shoes', 'badminton shoes']
]

print(things)
print(things[1])
print(things[2])
print(things[1][1])
print(things[2][0])
print(things[0][1])

contoh = [
    [
        ['hello', 'apa', 'kabar'],
        [1, 2, 3]
    ],
    [
        [True, False, [1, [2, 3]]]
    ]
]

print(contoh)
print(contoh[0][1][1])
print(contoh[1][0][2][1][1])
