'''
Dictionary adalah suatu tipe data yang dapat menyimpan lebih dari satu data di dalamnya, sama seperti list.
perbedaannya terletak pada indexnya dimana klo di dictionary disebut key and value
'''

# cara 1
dictionaryContoh1 = {
    'nama': 'Budi',
    'usia': 25,
    'pekerjaan': 'Developer'
}

print(dictionaryContoh1, type(dictionaryContoh1))

# cara 2
dictionaryContoh2 = dict(nama='Andi', usia=27, pekerjaan='Data Scientist')
print(dictionaryContoh2, type(dictionaryContoh2))

print("=" * 50)
# akses dictionary
dictionaryContoh = {
    'nama': 'Budi',
    'usia': 25,
    'pekerjaan': 'Developer',
    'menikah': False
}

print(dictionaryContoh['nama'])
print(dictionaryContoh['usia'])
print(dictionaryContoh.get('pekerjaan'))
print(dictionaryContoh.get('menikah'))

print("=" * 50)
# change data
dictionaryContoh['usia'] = 27
print(dictionaryContoh)

print("=" * 50)
# add data
dictionaryContoh['kelamin'] = 'pria'
print(dictionaryContoh)

print("=" * 50)
# delete data

del dictionaryContoh['kelamin']  # removes key-value pair for kelamin key
dictionaryContoh.pop('usia')  # removes key-value pair for usia key
dictionaryContoh.popitem()  # removes the last inserted item

print(dictionaryContoh)
dictionaryContoh.clear()  # empties the dictionary

print(dictionaryContoh)

print("=" * 50)
# for loop
dictionaryContoh = {
    'nama': 'Budi',
    'usia': 25,
    'pekerjaan': 'Developer',
    'menikah': False
}

for key in dictionaryContoh:
    print("{} = {}".format(key, dictionaryContoh[key]))

hasil = dictionaryContoh.keys()
print(hasil, type(hasil))

for key in dictionaryContoh.keys():
    print("{} = {}".format(key, dictionaryContoh[key]))

hasil = dictionaryContoh.values()
print(hasil, type(hasil))

for val in dictionaryContoh.values():
    print(val)

hasil = dictionaryContoh.items()  # hasil dri items berupa tuple
print(hasil, type(hasil))
#dict_items([('nama', 'Budi'), ('usia', 25), ('pekerjaan', 'Developer'), ('menikah', False)])

for key, val in dictionaryContoh.items():
    print("{} = {}".format(key, val))  # print key dan values sekaligus

print("=" * 50)
# check keys in dictionary
check = 'kelamin' in dictionaryContoh
print(check)

if 'usia' in dictionaryContoh:
    print("ada bro")
else:
    print("sorry gga ada hehe")

'''
di dictionary bisa jg pakai fungsi len()
print(len(dictionaryContoh))

copy a dictionary bisa juga sama kaya list tuple
pake .copy()
newDictionary = dictionaryContoh.copy()

'''

print("=" * 50)
# dict inside dict
things = {
    'food1': {
        'name': 'Ramen',
        'price': 25000
    },
    'food2': {
        'name': 'Pizza',
        'price': 30000
    },
    'food3': {
        'name': 'Spaghetti',
        'price': 20000
    }
}

print(things['food1'])
print(things['food2']['name'])

contoh = {
    'anggota': [
        {
            'nama': 'Andi',
            'usia': 21,
            'hobby': ('Main Basket', 'Nonton Film', 'Denger Musik')
        },
        {
            'nama': 'Budi',
            'usia': 22,
            'hobby': ('Nonton Drakor', 'Main Futsal', 'Makan Sushi')
        }
    ],
    'ketua': {
        'nama': 'Sultan',
        'usia': 27,
        'hobby': ('Main Kelereng', 'Nonton Anime', 'Makan')
    }
}

print(contoh['ketua']['nama'])
# pertama akses key dari 'anggota' dlu baru index dari list nya [1]
print(contoh['anggota'][1])
print(contoh['anggota'][0]['hobby'])
# habis dari key hobby kita harus akses index dari si tupplenya
print(contoh['anggota'][1]['hobby'][2])
