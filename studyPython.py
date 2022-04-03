numbers = [2, 4, 6, 8, 10, 12, 14]

for left in range(int(len(numbers)/2)):
    righ = len(numbers) - left -1

    temp = numbers[left]
    numbers[left] = numbers[righ]
    numbers[righ] = temp

print("뒤집어진 리스트: " + str(numbers))