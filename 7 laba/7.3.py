sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
result = [num for num in sequence if 10 <= num <= 99]
result.sort()
print("Положительные двузначные числа, отсортированные по возрастанию:", result)