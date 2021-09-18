text = "Hallo apa kabar?"
hurufDilewati = input(
    "Masukkan huruf yang ingin dilewati pada text ({}) : ".format(text))

for c in text:
    if(c == hurufDilewati):
        continue
    print(c)
