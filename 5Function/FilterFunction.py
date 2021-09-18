list1 = [1, 2, 3, 4, 5]


def angkaGenap(angka):
    return angka % 2 == 0


hasilFilter = filter(angkaGenap, list1)
print(hasilFilter, type(hasilFilter))

hasilFilterList = list(hasilFilter)
print(hasilFilterList)  # [2, 4]

hasilFilterList1 = list(filter(lambda angka: angka % 2 == 0, list1))
print(hasilFilterList1)  # [2, 4]

print("=" * 50)
# membuat function filter buatan sendiri, tiruan dri filter di python


def filterDuplikat(fn, collection):
    newCollection = []
    for item in collection:  # nah item nya itu ngambil dari list1
        if(fn(item)):  # fn disini itu nanti nyambungnya ke function angkaGenapFilter
            # saat kondisi if nya jadi true bahwa itu angka genap
            newCollection.append(item)
    return newCollection  # maka akan ditambahkan ke list newCollection = []


list1 = [1, 2, 3, 4, 5]


def angkaGenapFilter(angka):
    return angka % 2 == 0


# saat ini dijalankan, maka akan terhubung ke parameter (fn, collection)
newList = filterDuplikat(angkaGenapFilter, list1)
print(newList)  # [2, 4]

print(filterDuplikat(lambda angka: angka % 2 == 0, list1))  # [2, 4]
