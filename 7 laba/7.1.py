a = input("Введите строку: ")

words = a.split()
summ_str = sum(len(word) for word in words)

print("Сумма длин всех строк:", summ_str)