# contoh 1
jmlPutaran = 0
while(True):
    jmlPutaran += 1
    print("Putaran {}".format(jmlPutaran))

    inputan = input("Masukkan yes untuk keluar : ")
    if(inputan == "yes"):
        break

# contoh 2
text = "Hallo apa kabar?"
hurufDicari = input(
    "Masukkan huruf yang ingin dicari pada text ({}) : ".format(text))
index = 0

for c in text:
    if(c == hurufDicari):
        break
    index += 1

if(index == len(text)):
    print("Huruf {} tidak ditemukan".format(hurufDicari))
else:
    print("Huruf {} pertama ditemukan pada index ke {}".format(hurufDicari, index))
