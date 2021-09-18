'''
saat ini jumlah usia Andi dan Budi = 49th
dengan rasio usia Andi dan Budi = 0.4

berapa usia Andi dan Budi 2 tahun lagi?
'''

# usiaAndi + usiaBudi = 49
# rasio usiaAndi dan usiaBudi = 0.4 = 4/10 => 4 : 10 => 2 : 5
# rasio usiaAndi = 2, rasio usiaBudi = 5
# total rasio = 2 + 5 = 7
# usiaAndi = totalUmur * (rasio usiaAndi / total rasio)
# usiaBudi = totalUmur * (rasio usiaBudi / total rasio)

totalUmur = 49
ratioAndi = 2
ratioBudi = 5
ratioTotal = 7

usiaAndi = totalUmur * (ratioAndi / ratioTotal)
usiaBudi = totalUmur * (ratioBudi / ratioTotal)

print('usia Andi sekarang = {}'.format(usiaAndi))
print('usia Budi sekarang = {}'.format(usiaBudi))

print('usia Andi 2 tahun lagi = ' + str(usiaAndi + 2))
print('usia Budi 2 tahun lagi = ' + str(usiaBudi + 2))
