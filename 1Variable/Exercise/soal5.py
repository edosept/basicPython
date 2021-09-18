'''
Jarak mobil A & B = 120 km
A berjalan 60km/h dari timur
B berjalan 40km/h dari barat

A & B start pukul 9 WIB

Jam berapa A & B bertabrakan?
'''

# Dua mobil A dan B melaju berlawanan arah dan akan bertabrakan
# kita dapat menghitung waktunya dengan menjumlahkan kecepatan dari kedua kendaraan tersebut
# lalu kemudian cari tahu dengan total kecepatan yang dimiliki
# berapa waktu yang dibutuhkan untuk menempuh jarak tertentu

# 60km/h + 40 km/h = 100km/h
# dengan kecepatan 100km/h. Berapa waktu yang dibutuhkan untuk menempuh jarak 120km?
# 120 / 100 = 1.2 jam
# 1.2 * 60 = 72 menit => 60 menit + 12 menit
# 9:00 WIB => 10:12
# waktu bertemu jam 10 menit ke 12

import math

jamAwal = 9
jarakKM = 120

kecepatanTotalKMperJam = 100
kecepatanTotalKMperDetik = kecepatanTotalKMperJam/3600

detikTotal = jarakKM / kecepatanTotalKMperDetik
lamaJam = math.floor(detikTotal / 3600)
lamaMenit = math.floor((detikTotal % 3600) / 60)
lamaDetik = math.floor((detikTotal % 3600) % 60)

print('Lama waktu ' + str(lamaJam) + ' jam, ' +
      str(lamaMenit) + ' menit, ' + str(lamaDetik) + ' detik')
print('Tabrakannya pukul {}:{}:{}'.format(
    jamAwal + lamaJam, lamaMenit, lamaDetik))
