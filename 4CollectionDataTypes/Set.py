'''
Set adalah sebuah tipe data yang dapat menyimpan data lebih dari satu.
sama seperti kawan kawannya, perbedaannya dia tidak mempunyai index.

Dan di set tidak ada data yang duplikat.
Dan data data yang disimpan dalam tipe data set itu tidak memiliki urutan.

Kita membutuhkan set biasanya dipakai untuk menghilangkan duplikat pada kumpulan data.
dan set juga bisa digunakan seperti melakukan operasi himpunan seperti yang ada pada matematika.

Set dibungkus sepasang {} sama seperti dictionary,
tetapi di dalamnya hanya berisikan value dari item-itemnya saja tidak ada key seperti di dictionary.
'''

setContoh = {'The Avengers', 'Iron Man 3',
             'Avengers : Age of Ultron', 'Iron Man 3', 20, False}
print(setContoh, type(setContoh))
# {False, 20, 'The Avengers', 'Avengers : Age of Ultron', 'Iron Man 3'} <class 'set'>
# urutan dari data set tampilnya akan selalu acak
# dan apabila ada data duplikat maka akan dihapus

print("=" * 50)
list1 = ['Budi', 2, 2, 'Ceci']
tuple1 = (False, 1, 'Andi', False)
dictionary1 = {
    'nama': 'Coder',
    'usia': 25,
    'pekerjaan': 'Coder',
    'menikah': False
}
# create set from list, tuple, dict
setList = set(list1)
setTuple = set(tuple1)
# klo cuma gini panggil variable dia auto akses keynya
setDict = set(dictionary1)
# tapi klo pake .values baru dia akses valuesnya
setDictVal = set(dictionary1.values())

print(setList)  # {'Ceci', 2, 'Budi'}
print(setTuple)  # {False, 1, 'Andi'}
print(setDict)  # {'menikah', 'pekerjaan', 'usia', 'nama'}
print(setDictVal)  # {False, 25, 'Coder'}

''' akses data pada set tidak bisa pakai index,
tetapi kita bisa pakai for loop untuk melakukan iterasi pada setiap itemnya
'''
print("=" * 50)
setContoh = {'The Avengers', 'Iron Man 3',
             'Avengers : Age of Ultron', 'Iron Man 3'}

for item in setContoh:
    print(item)

'''
kita jg dapat mengecek apakah suatu data terdapat pada suatu set
sama seperti kawan kawannya bisa pakai keyword in
'''
# add data set
print("=" * 50)
'''
kita tidak bisa mengedit item atau data yang ada pada set,
tetapi kita bisa menambahkan datanya
'''
# method add itu hanya menambahkan 1 item saja
setContoh.add('Iron Man')
print(setContoh)
# {'The Avengers', 'Iron Man 3', 'Iron Man', 'Avengers : Age of Ultron'}

# method update bisa menambahkan beberapa item sekaligus
# plus klo method update pakai kurung kurawal
setContoh.update({'Iron Man 3', 'Hulk'})
print(setContoh)
#{'Iron Man 3', 'Hulk', 'Avengers : Age of Ultron', 'The Avengers', 'Iron Man'}
# 'Iron Man 3' hanya ditampilkan satu karena set tidak bisa duplikat

print("=" * 50)
# delete data
'''
perbedaan remove dan discard adalah
kalau menggunakan method remove bila data yang ingin dihapus tidak ada pada setnya, maka akan menghasilkan error.
kalau method discard dia tidak menghasilkan error walaupun datanya tidak ada.

ada juga method pop dia gga kaya di list dan kawankawannya yang hapus item terakhir,
tapi dia menghapus itemnya secara acak dalam suatu set

ada juga method clear yg fungsinya sama dengan list dan kawan kawan.
'''
setContoh = {'The Avengers', 'Iron Man 3',
             'Avengers : Age of Ultron', 'Hulk', 'Wonder Woman'}

setContoh.remove('The Avengers')
print(setContoh)

setContoh.discard('Hulk')
print(setContoh)

setContoh.pop()
print(setContoh)

setContoh.clear()
print(setContoh)

'''
di set bisa jg pakai fungsi len()
print(len(setContoh))
'''

print("=" * 50)
# join data sets
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers : Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers'}

setGabungan = setMovie1.union(setMovie2)
# {'Hulk', 'The Avengers', 'Iron Man 3', 'Titanic', 'Avengers : Age of Ultron'}
print(setGabungan)
# karena set tidak menerima duplikasi, maka saat digabungkan pun tidak ada data duplikat

print("=" * 50)
# get difference between 2 sets
'''
difference --> kayak mencari perbedaan data dari set satu dengan yang lainnya
- method difference itu menciptakan set baru dan set yang dijalankan tidak akan berubah datanya
- method difference_update tidak akan menciptakan set baru,
melainkan akan merubah item data dari set dimana dia dipanggil menjadi item data
- data yang duplikat tidak akan dipanggil
'''
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers : Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setMovie3 = setMovie1.difference(setMovie2)
# method difference hanya akan menampilkan data yg hanya dimiliki oleh setMovie1 saja
print(setMovie3)
#{'Iron Man 3', 'Avengers : Age of Ultron'}
print(setMovie1)
#{'Hulk', 'Iron Man 3', 'The Avengers', 'Avengers : Age of Ultron'}
setMovie1.difference_update(setMovie2)
print(setMovie1)
#{'Iron Man 3', 'Avengers : Age of Ultron'}

print("=" * 50)
# get symmetric difference between 2 sets
'''
perbedaan data pada 2 set secara simetris,
klo simetris itu semua perbedaan dari kedua set tersebut diambil,
klo yang difference biasa itu kan ngga dia cuma membandingkan dan yg diambil cuma set satunya doang
'''
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers : Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setMovie3 = setMovie1.symmetric_difference(setMovie2)
print(setMovie3)
#{'Avengers : Age of Ultron', 'Iron Man 3', 'Titanic'}
print(setMovie1)
#{'The Avengers', 'Avengers : Age of Ultron', 'Hulk', 'Iron Man 3'}

setMovie1.symmetric_difference_update(setMovie2)
print(setMovie1)
#{'Iron Man 3', 'Avengers : Age of Ultron', 'Titanic'}

print("=" * 50)
# get intersection between 2 sets
'''
klo difference tadi ambil data yang beda,
nah klo si intersection ini dia mengambil data yang sama
'''
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers : Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setMovie3 = setMovie1.intersection(setMovie2)
print(setMovie3)
#{'The Avengers', 'Hulk'}
print(setMovie1)
#{'The Avengers', 'Iron Man 3', 'Hulk', 'Avengers : Age of Ultron'}
setMovie1.intersection_update(setMovie2)
print(setMovie1)
#{'The Avengers', 'Hulk'}

print("=" * 50)
# check disjoint, subset, and superset
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers : Age of Ultron', 'Hulk'}
setMovie2 = {'The Avengers', 'Hulk'}

# apakah set1 dan set2 tidak memiliki data yg sama?
checkDisjoint = setMovie1.isdisjoint(setMovie2)
# apakah smua data yg dimiliki set2 dimiliki jg oleh set1?
checkSubset = setMovie2.issubset(setMovie1)
# subset dan superset keduanya berhubungan, cuma beda arah manggilnya aja
checkSuperset = setMovie1.issuperset(setMovie2)

print(checkDisjoint)  # False
print(checkSubset)  # True
print(checkSuperset)  # True
