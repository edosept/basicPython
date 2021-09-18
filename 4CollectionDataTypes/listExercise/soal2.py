numbers = [41, 5, 1, 3, 89, 32]

print('List Sebelum Di Sort = {}'.format(numbers))

for i in range(len(numbers) - 1):  # range(5) brarti mulai index ke 0,1,2,3,4
    for j in range(i+1, len(numbers)):  # range(1,6) brarti mulai index ke 1,2,3,4,5
        if(numbers[i] > numbers[j]):  # cek apakah numbers index ke 0 > index ke 1? dst
            # klo ya maka posisi item di balik
            numbers[i], numbers[j] = numbers[j], numbers[i]
        # misal itu kan si numbers index ke0 yaitu 41 benar lebih besar dari index ke1 yaitu 5
        # maka akan di sort asc
# si for loop ini sampe selesai cek kondisinya maka baru print hasilnya jadi [1, 3, 5, 32, 41, 89]
print('List Setelah Di Sort = {}'.format(numbers))

# tambahan klo mau di sort desc dari terbesar ke terkecil
# rubah jadi kurang dari --> if(numbers[i] < numbers[j]):
