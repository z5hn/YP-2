class Numbers:
    def data(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def show(self):
        print(f"Первое число: {self.num1}")
        print(f"Второе число: {self.num2}")

    def change_number(self, new1, new2):
        self.num1 = new1
        self.num2 = new2

    def summ(self):
        return self.num1 + self.num2
    def mx(self):
        return max(self.num1, self.num2)

pari = Numbers()

pari.data (22, 33)

print("Исходные значения:")
pari.show()

pari.change_number(52, 42)
print("\nПосле изменения:")
pari.show()


print("\nСумма чисел:", pari.summ())

print("\nНаибольшее число:", pari.mx())

