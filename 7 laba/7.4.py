class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин."

    def __lt__(self, other):
        return self.duration < other.duration


fitness_sessions = [
    FitnessCenter("A001", 2025, 5, 60),
    FitnessCenter("A002", 2025, 5, 45),
    FitnessCenter("B003", 2025, 5, 90),
    FitnessCenter("B004", 2025, 5, 30)
]

longest = max(fitness_sessions)
shortest = min(fitness_sessions)

print("Самое продолжительное занятие:")
print(longest)
print("\nСамое короткое занятие:")
print(shortest)