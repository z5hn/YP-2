numbers = list(map(int, input("Введите целочисленную последователность:").split()))
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
print(positive_numbers)