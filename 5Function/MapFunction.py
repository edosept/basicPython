'''
Map Function itu digunakan untuk mengubah bentuk atau value,
dari data data yang disimpan pada suatu collection data type,
tanpa merubah banyaknya data pada collection data type tersebut
'''
list1 = [1, 2, 3, 4, 5]


def kali2(angka):
    return angka * 2


hasilMap = map(kali2, list1)
print(hasilMap, type(hasilMap))

hasilMapList = list(hasilMap)
print(hasilMapList)

hasilMapList = list(map(lambda angka: angka * 2, list1))
print(hasilMapList)

print("=" * 50)
# membuat function map buatan sendiri, tiruan dri map di python


def mapDuplikat(fn, collection):
    newCollection = []
    for item in collection:
        newCollection.append(fn(item))
    return newCollection


list1 = [1, 2, 3, 4, 5]


def ubah(angka):
    return 'Angka {}'.format(angka)


newList = mapDuplikat(ubah, list1)
print(newList)  # ['Angka 1', 'Angka 2', 'Angka 3', 'Angka 4', 'Angka 5']

print(mapDuplikat(lambda angka: 'Angka {}'.format(angka), list1))
#['Angka 1', 'Angka 2', 'Angka 3', 'Angka 4', 'Angka 5']
