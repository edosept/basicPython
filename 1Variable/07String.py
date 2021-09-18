# String apapun yang diapit dengan tanda kutip itu merupakan string
# ini semua merupakan tipe data string gga peduli itu angka atau huruf karena semuanya diapit tanda kutip
# "Happy Weekend"
# "25 adalah bilangan ganjil"
# "12345"
# "True"

kutipSatu = 'kutip satu ("Im Hulk")'
kutipDua = "kutip dua (I'm Iron Man)"
kutipTiga = '''
"Im Hulk"
I'm Iron Man

' " '
'''

print(kutipSatu, type(kutipSatu))
print(kutipDua, type(kutipDua))
print(kutipTiga, type(kutipTiga))

print("="*50)
# Escape character --> garis miring terbalik misal \ text \
esc1 = "Salam kenal \"teman-teman\", mari kita belajar bersama."
print(esc1)

esc2 = 'Hello I\'m Edo'
print(esc2)

esc3 = 'This is backslash => \\'
print(esc3)

esc4 = 'Hello Guys, \nSelamat datang di Marvel Studios!'
print(esc4)

esc5 = '\tHello Guys!'
print(esc5)

esc6 = 'Hello Guys\b!'  # \b backspace menghapus huruf sebelumnya
print(esc6)

print("="*50)
# string method len dan kawan kawan
text = "Hallo Apa Kabar?"

panjangString = len(text)
print(panjangString, type(panjangString))

indexApa = text.index('Apa')
print(indexApa, type(indexApa))

indexPertama = text.index('a')
print(indexPertama, type(indexPertama))

hasilSplit1 = text.split(' ')
print(hasilSplit1, type(hasilSplit1))

hasilSplit2 = text.split('a')
print(hasilSplit2, type(hasilSplit2))

versiHurufKecil = text.lower()
print(versiHurufKecil, type(versiHurufKecil))

versiHurufBesar = text.upper()
print(versiHurufBesar, type(versiHurufBesar))

hurufPertamaCapital = text.capitalize()
print(hurufPertamaCapital)

print("="*50)
# string slicing
text = "I'm edo, nice to meet you"

print(text[1])  # '
print(text[2:])  # m edo, nice to meet you
print(text[:4])  # I'm
print(text[2:5])  # m e
print(text[:])  # I'm edo, nice to meet you
print(text[-1])  # u
print(text[-3:-1])  # yo

print("="*50)
# string concatenate
a = "Apel"
b = "Jeruk"

c = a + b
print(c)  # ApelJeruk

d = a + " " + b + " Mangga"
print(d)  # Apel Jeruk Mangga

e = str(5) + " " + a  # concatenate wajib tipe data sama
print(e)  # 5 Apel

print("="*50)
# string format
umur = 25
nama = "edo"
txt = "Nama saya {}, saya berumur {}".format(nama, umur)
print(txt)

jumlahApel = 3
jumlahJeruk = 5
jumlahMangga = 7
pembelian = "Saya mau beli {jmlApel} Apel, {jmlMangga} Mangga, dan {jmlJeruk} Jeruk"
print(pembelian.format(jmlMangga=7, jmlJeruk=jumlahJeruk, jmlApel=jumlahApel))

print("="*50)
# string cek, output True False
txt = "Nama saya edo"
a = "aya" in txt
b = "maya" in txt
print(a, type(a))
print(b, type(b))

c = "aya" not in txt
d = "maya" not in txt
print(c, type(c))
print(d, type(d))
