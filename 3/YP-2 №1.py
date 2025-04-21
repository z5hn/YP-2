class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def show_info(self):
        print(f"Имя: {self.name}, Фамилия: {self.surname}, Ставка: {self.rate}, Дней: {self.days}")

    def GetSalary(self):
        return self.rate * self.days


worker1 = Worker("Oleg", "Nichiporenko", 10000, 20)
worker2 = Worker("Timofeiy", "Gordon", 8000, 15)
worker3 = Worker("Roman", "Pechkin", 12000, 24)

while True:
    try:
        choice = int(input("\nВыберите действие:"
                           "\n1 - Вывести работника 1"
                           "\n2 - Вывести работника 2"
                           "\n3 - Вывести работника 3"
                           "\n4 - Вывести всех работников"
                           "\n5 - Вывести их зарплату за месяц"
                           "\n6 - Выход из программы\n> "))

    except ValueError:
        print("Введите число от 1 до 6.")
        continue

    match choice:
        case 1:
            worker1.show_info()
        case 2:
            worker2.show_info()
        case 3:
            worker3.show_info()
        case 4:
            worker1.show_info()
            worker2.show_info()
            worker3.show_info()
        case 5:
            print(f"Зарплата {worker1.name}: {worker1.GetSalary()} руб.")
            print(f"Зарплата {worker2.name}: {worker2.GetSalary()} руб.")
            print(f"Зарплата {worker3.name}: {worker3.GetSalary()} руб.")
        case 6:
            print("Выход из программы.")
            break
        case _:
            print("Неверный выбор! Введите число от 1 до 6.")
