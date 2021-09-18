# hasilnya true
hasil1 = 5 == 5
hasil2 = 7 != 5
hasil3 = 5 > 2
hasil4 = 2 < 5
hasil5 = 5 >= 5
hasil6 = 5 <= 5

print(hasil1, type(hasil1))
print(hasil2, type(hasil2))
print(hasil3, type(hasil3))
print(hasil4, type(hasil4))
print(hasil5, type(hasil5))
print(hasil6, type(hasil6))
print("=" * 50)
# hasilnya false
print(4 == 5)
print(5 != 5)
print(2 > 5)
print(5 < 2)
print(5 >= 7)
print(5 <= 2)

print("=" * 25 + "logical and")
# logical and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

hasil1 = 5 < 7 and 4 >= 4
hasil2 = 5 < 7 and 4 >= 5
hasil3 = 2 > 5 and 5 == 5
hasil4 = 5 != 5 and 4 == 7

print('hasil1 = ', hasil1, type(hasil1))
print('hasil2 = ', hasil2, type(hasil2))
print('hasil3 = ', hasil3, type(hasil3))
print('hasil4 = ', hasil4, type(hasil4))

print("=" * 25 + "logical or")
# logical or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

hasil1 = 5 < 7 or 4 >= 4
hasil2 = 5 < 7 or 4 >= 5
hasil3 = 2 > 5 or 5 == 5
hasil4 = 5 != 5 or 4 == 7

print('hasil1 = ', hasil1, type(hasil1))
print('hasil2 = ', hasil2, type(hasil2))
print('hasil3 = ', hasil3, type(hasil3))
print('hasil4 = ', hasil4, type(hasil4))

print("=" * 50 + "logical not")
# logical not
print(not(True))
print(not(False))

hasil1 = not((5 > 2 or 4 == 5) and 5 != 5)
hasil2 = not('hello' == "hello")
hasil3 = not(4 > 3 and 'apa' == "Apa")
hasil4 = not(3 > 5 or (7 != 8 and "kari" != "kuri"))
hasil5 = not(5 != 5 and 7 > 2)

print("hasil1 = ", hasil1, type(hasil1))
print("hasil2 = ", hasil2, type(hasil2))
print("hasil3 = ", hasil3, type(hasil3))
print("hasil4 = ", hasil4, type(hasil4))
print("hasil5 = ", hasil5, type(hasil5))
