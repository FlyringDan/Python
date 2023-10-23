numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_ = 0
for i in range(len(numbers)):
    if numbers[i] != None:
        sum_ += numbers[i]
numbers[4] = sum_ / len(numbers)
print("Измененный список:", numbers)
