setMovieKesukaanKu = set(input('Masukkan 5 Film Kesukaan anda dipisahkan dengan koma : ').split(','))
setMovieKesukaanTemanKu = set(input('Masukkan 5 Film Kesukaan teman anda dipisahkan dengan koma : ').split(','))

setMovieYangSama = setMovieKesukaanKu.intersection(setMovieKesukaanTemanKu)
print("Kesukaan Film kalian yang sama sebesar {}%".format((len(setMovieYangSama)/len(setMovieKesukaanKu)) * 100))
