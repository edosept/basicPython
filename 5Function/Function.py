# Function Without Input(parameter) & Output(return)
def salam():
    print('Hallo apa kabar?')
    print('Semoga hari anda menyenangkan!')


salam()

print("=" * 50)
# Function With Input(parameter) but Without Output(return)


def salamBalik(nama, usia):
    print('Hallo perkenalkan nama saya {}, dan usia saya {}'.format(nama, usia))
    print('Senang bertemu dengan anda!')


salamBalik('Andi', 25)
# klo gga mau sesuai urutan dari parameter, kita bisa buat begini:
salamBalik(usia=23, nama='Budi')
'''
Parameter or Argument ?
#Parameter = (nama, usia)
#Argument = ('Andi', 25)
'''

print("=" * 50)
# Default Parameter


def salamBalik2(nama='Unknown', usia=0):
    if(nama == 'Unknown' and usia > 0):
        print('Saya berusia {}'.format(usia))
    elif(nama != 'Unknown' and usia == 0):
        print('Hello nama saya {}'.format(nama))
    elif(nama != 'Unknown' and usia > 0):
        print('Hallo perkenalkan nama saya {}, dan usia saya {}'.format(nama, usia))

    print('Senang bertemu dengan anda!')


salamBalik2(usia=25)
salamBalik2(nama='Ceci')
salamBalik2(usia=20, nama='Dodi')

print("=" * 50)
# Function With Input(parameter) & Output(return)
# contoh1


def tambah(angka1, angka2):
    return angka1 + angka2


hasil = tambah(5, 4)
print(hasil)
print(tambah(10, 2))

# contoh2


def coba(nama):
    print('Selamat datang {} di Toko Kue Bahagia!'.format(nama))
    print('Kuenya dijamin bikin bahagia loh!')

    while(True):
        mau = input('Mau coba kue ini? : ')
        if(mau == 'yes'):
            print('Thank you! silahkan ini kuenya')
            return 'Kue Cokelaat'
        elif(mau == 'ggamau!'):
            break
        print('Anda yakin?')
    print('Semoga anda selalu bahagia dan sampai jumpa lagi :)')


kue = coba('edo')
print(kue, type(kue))  # return 'Kue Cokelaat'
