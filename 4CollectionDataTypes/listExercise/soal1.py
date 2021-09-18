numbers = [41, 5, 1, 3, 89, 32]
minVal = numbers[0]
maxVal = numbers[0]

for num in numbers:
    if(num < minVal):  # membandingkan dari setiap data numbers
        minVal = num  # sampai ketemu angka paling kecilnya maka dia akan jadi minvalnya
    if(num > maxVal):
        maxVal = num

print("Numbers = {}".format(numbers))
print("Minimum value = {}".format(minVal))
print("Maximum value = {}".format(maxVal))
