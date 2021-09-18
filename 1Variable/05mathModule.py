import math

# ceil method --> pembulatan keatas
print("ceil method")
x = 4.2
x = math.ceil(x)
print(x)
print(math.ceil(7.1))
print("="*50)

# floor method --> pembulatan kebawah
print("floor method")
x = 4.8
x = math.floor(x)
print(x)
print(math.floor(7.9))
print("="*50)

# fabs method --> mengembalikan nilai absolutnya --mutlak tidak boleh negatif
print("fabs method")
x = -4.5
x = math.fabs(x)
print(x)
print(math.fabs(5.2))
print(math.fabs(7))
print(math.fabs(-7))
print("="*50)

# pow method --> akan memangkatkan inputan pertama dgn berdasarkan inputan keduanya
print("pow method")
x = 4
y = 3
hasil = math.pow(x, y)
print(hasil)
print(math.pow(2, 3))
print(2 ** 3)
print("="*50)

# sqrt method --> akar dari nilai, misal akar dari 25 itu 5
print("sqrt method")
x = 25
x = math.sqrt(x)
print(x)
print(math.sqrt(9))
print("="*50)
# pi constant --> angka tetap 3.14
print("pi constant")
radius = 3
#luas = pi * r**2
luas = math.pi * math.pow(radius, 2)
print(luas)
