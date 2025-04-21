class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days


    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_rate(self):
        return self.rate

    def get_days(self):
        return self.days

    def get_data(self):
        print(f"{self.name} {self.surname}, ставка: {self.rate}, дней: {self.days}")

    def GetSalary(self):
        return self.rate * self.days


worker1 = Worker("Oleg", "Nichiporenko", 10000, 20)
worker2 = Worker("Timofei", "Gordon", 8000, 15)
worker3 = Worker("Roman", "Pechkin", 12000, 24)


while True:
    try:
        choice = int(input("\nВыберите действие:"
                           "\n1 - Вывести работника 1"
                           "\n2 - Вывести работника 2"
                           "\n3 - Вывести работника 3"
                           "\n4 - Вывести всех работников"
                           "\n5 - Вывести зарплату всех работников"
                           "\n6 - Выход\n> "))
    except ValueError:
        print("Введите число от 1 до 6.")
        continue

    match choice:
        case 1:
            worker1.get_data()
        case 2:
            worker2.get_data()
        case 3:
            worker3.get_data()
        case 4:
            worker1.get_data()
            worker2.get_data()
            worker3.get_data()
        case 5:
            print(f"Зарплата {worker1.get_name()}: {worker1.GetSalary()} руб.")
            print(f"Зарплата {worker2.get_name()}: {worker2.GetSalary()} руб.")
            print(f"Зарплата {worker3.get_name()}: {worker3.GetSalary()} руб.")
        case 6:
            print("Выход из программы.")
            break
        case _:
            print("Неверный выбор!")
