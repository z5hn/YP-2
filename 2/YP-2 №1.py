class Student:
    def set_data(self, last_name, date_of_birth, number_group, grades):
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.number_group = number_group
        self.grades = grades

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

    def change_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

    def change_number_group(self, new_group):
        self.number_group = new_group

    def info(self):
        print(f"Фамилия: {self.last_name}")
        print(f"Дата рождения: {self.date_of_birth}")
        print(f"Номер группы: {self.number_group}")
        print(f"Оценки: {self.grades}")

student1 = Student()
student1.set_data("Петров", "09.03.2007", "Группа 643", [5, 5, 5, 4, 4])

student2 = Student()
student2.set_data("Царев", "10.11.2005", "Группа 555", [3, 3, 4, 3, 5])

student3 = Student()
student3.set_data("Иванов", "25.10.1999", "Группа 777", [5, 5, 5, 5, 5])


student1.change_last_name("Смирнов")
student1.change_date_of_birth("04.07.2000")
student1.change_number_group("Группа 890")


students = [student1, student2, student3]

search_last_name = input("Введите фамилию студента: ")
search_date_of_birth = input("Введите дату рождения (Например 11.11.1111): ")

found = False
for student in students:
    if student.last_name == search_last_name and student.date_of_birth == search_date_of_birth:
        print("\nНайден студент:")
        student.info()
        found = True
        break

if not found:
    print("Студента с такими данными нету")
