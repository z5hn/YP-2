class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start    # Дата начала (строка или datetime)
        self.DateFinish = date_finish  # Дата окончания (строка или datetime)
        self.Description = description # Описание занятия

    def __str__(self):
        return f"Начало: {self.DateStart}, Окончание: {self.DateFinish}, Описание: {self.Description}"


tasks = [
    Task("2023-10-01 08:00", "2023-10-01 10:30", "Экзамен по Python"),
    Task("2023-10-01 12:00", "2023-10-01 15:00", "Практика по ОАиП"),
    Task("2023-10-02 14:00", "2023-10-02 15:30", "Семинар по ОПБД"),
    Task("2023-10-03 11:00", "2023-10-03 13:00", "Встреча с командой"),
    Task("2023-10-04 12:00", "2023-10-04 14:00", "Разбор заданий")
]

latest_task = tasks[0]

for task in tasks[1:]:  # Проверяем остальные занятия
    if task.DateFinish > latest_task.DateFinish:
        latest_task = task

print("Занятие, которое заканчивается позже всех:")
print(latest_task)