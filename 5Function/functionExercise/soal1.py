def ganjilGenap(angka) :
    if(angka % 2 == 0) :
        return 'Genap'
    return 'Ganjil'

def ubahJadiGanjilGenap(listAngka) :
    return list(map(ganjilGenap, listAngka))

list1 = [1,3,4,5]
list2 = [22,17,19,20,14]
list3 = [1,3,5]
list4 = [2,4,6]

list1 = ubahJadiGanjilGenap(list1)
list2 = ubahJadiGanjilGenap(list2)
list3 = ubahJadiGanjilGenap(list3)
list4 = ubahJadiGanjilGenap(list4)

print(list1)
print(list2)
print(list3)
print(list4)