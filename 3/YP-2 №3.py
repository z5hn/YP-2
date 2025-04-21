class Calculation:
    def __init__(self, calculationLine):
        self.calculationLine = calculationLine

    def SetCalculationLine(self, new_calculationLine):
        self.calculationLine = new_calculationLine

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        print(f"Значение: {self.calculationLine}")

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        return ""

    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]


value = Calculation("<>")


while True:
    try:
        choice = int(input("\nВыберите действие:"
                           "\n1 - Изменить значение"
                           "\n2 - Добавить в конце строки символ"
                           "\n3 - Вывести значение свойства"
                           "\n4 - Получение последнего символа"
                           "\n5 - Удаление последнего символа из строки"
                           "\n6 - Выход из программы\n> "))
    except ValueError:
        print("Введите число!!!")
        continue

    match choice:
        case 1:
            calculationLine1 = input("Введите новое значение: ")
            value.SetCalculationLine(calculationLine1)
        case 2:
            symbol = input("Добавьте символ в конец строки: ")
            value.SetLastSymbolCalculationLine(symbol)
        case 3:
            value.GetCalculationLine()
        case 4:
            last_symbol = value.GetLastSymbol()
            print(f"Последний символ: {last_symbol}")
        case 5:
            value.DeleteLastSymbol()
            print("Последний символ удален.")
        case 6:
            print("Выход из программы.")
            break
        case _:
            print("Неверный выбор!")
