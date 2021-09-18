'''
Tuple sifatnya hampir sama dengan List
Perbedaannya terletak pada data data yang disimpan di dalamnya tidak bisa diubah,
jadi kita tidak dapat menambahkan, mengurangi, ataupun mengedit data yang ada pada Tuple.
Jadi kita kadang lebih memilih tuple untuk menyimpan suatu kumpulan data yang tidak boleh dan tidak akan berubah.
dan Tuple juga lebih menggunakan sedikit space di RAM dibandingkan List
'''

tupleContoh = ('hello', 1, 1, 3, True)

# tupleContoh[1] = 50 #TypeError: 'tuple' object does not support item assignment
# del tupleContoh[2] #TypeError: 'tuple' object doesn't support item deletion
# tupleContoh.append('test') #AttributeError: 'tuple' object has no attribute 'append'

'''
terbukti kita tidak dapat menambahkan, mengurangi, ataupun mengedit data yang ada pada Tuple.
jika kita ingin mengubah data pada Tuple ya kita harus casting dlu ke List
'''

listContoh = list(tupleContoh)
listContoh[1] = 50
del listContoh[2]
listContoh.append('test')

# baru kita balikin lg nih ke tuple hehe
tupleContoh = tuple(listContoh)
print(tupleContoh)  # ('hello', 50, 3, True, 'test')

print("=" * 50)
print("membuat tuple yang hanya memiliki satu item saja")
# klo item data nya cuma 1 itu harus ditambahkan tanda koma
tuple1 = ("hello",)
print(tuple1)
print(len(tuple1))
print(type(tuple1))

print("=" * 50)
print("tuple concatenate")
tupleContoh = ('hello', 1, 1, 3, True)
tupleCoba = (5, 'test', False)

# hanya bisa operator tambah saja untuk penggabungan
tupleGabungan = tupleContoh + tupleCoba
# tidak bisa extend kaya di list
print(tupleGabungan)

print("=" * 50)
print("tuple dua dimensi")
things = (
    ('red pen', 'blue pen'),
    ('analog clock', 'digital clock'),
    ['futsal shoes', 'badminton shoes']
)

print(things)
print(things[1])
print(things[2])
print(things[1][1])
print(things[2][0])

things[2][0] = 'basketball shoes'
print(things)
print(things[2])
print(things[2][0])
