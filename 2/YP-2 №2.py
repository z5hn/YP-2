class Train:
    def set_data(self, destination, train_number, time):
        self.destination = destination
        self.train_number = train_number
        self.time = time

    def change_destination(self, new_destination):
        self.destination = new_destination

    def change_train_number(self, new_number):
        self.train_number = new_number

    def change_time(self, new_time):
        self.time = new_time

    def info(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер поезда: {self.train_number}")
        print(f"Время отправления: {self.time}")

train1 = Train()
train1.set_data("Омск", "643", "10:30")

train2 = Train()
train2.set_data("Йошкар ола", "555", "16:00")

train3 = Train()
train3.set_data("Томск", "777", "20:00")


train1.change_destination("Владимир")
train1.change_time("15:00")
train1.change_train_number("900")


trains = [train1, train2, train3]


search_number = input("Введите номер поезда: ")

found = False
for train in trains:
    if train.train_number == search_number:
        print("\nНайден поезд:")
        train.info()
        found = True
        break

if not found:
    print("Поезд с таким номером не найден.")
