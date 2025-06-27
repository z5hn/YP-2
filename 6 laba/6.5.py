C = input("Введите символ C: ")
A = input("Введите последовательность A через пробел: ").split()

count = 0

for element in A:
    if len(element) > 1 and element.startswith(C) and element.endswith(C):
        count += 1

print(f"Количество элементов: {count}")