def filterGaji(listGaji) :
    return list(filter(lambda gaji : gaji * 95/100 > 9000000, listGaji))

list1 = [9100000,9800000,9500000,10300000,9300000]

list1 = filterGaji(list1) #filter itu ya hanya filter saja beda dengan map yg bisa mengubah data yg diberikan.

print(list1) #[9800000, 9500000, 10300000]