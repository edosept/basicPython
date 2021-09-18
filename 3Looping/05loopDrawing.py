stars = ""

for i in range(5):
    stars += "*\n"

print(stars)
print("=" * 50)

stars = ""
size = 5
# nested disini itu si for j bakal dijalanin trus loopnya sampai terpenuhi size = 5,
# baru dah dia pindah ke loop for i dan sampe selesai size = 5 baru print(stars)
for i in range(size):
    for j in range(size):
        stars += "* "
    stars += "\n"

print(stars)
print("=" * 50)

stars = ""
size = 5

for i in range(size):
    # selama si for j ini belum terpenuhi sama sizenya maka stars akan ditambahkan trus
    for j in range(1 + i):
        stars += "* "
    stars += "\n"

print(stars)
