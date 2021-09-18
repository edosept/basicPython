print("Selamat datang!")

umur = int(input("Masukkan umurmu: "))

if(umur >= 17):
    print("Anda sudah boleh bikin SIM")
    nama = input("Masukkan namamu: ")
    if(len(nama) > 1):
        print("Terima kasih {}".format(nama))
print("sampai jumpa!")
