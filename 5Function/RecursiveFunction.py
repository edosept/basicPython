'''
Recursive Function adalah kondisi dimana suatu function memanggil atau menjalankan dirinya sendiri.

'''


def countdown(counter):
    print(counter)
    counter -= 1

    if(counter >= 0):
        countdown(counter)
        print('counter = {}'.format(counter))


countdown(3)
