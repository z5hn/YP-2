class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин."

fitness_sessions = [
    FitnessCenter("A001", 2024, 1, 60),
    FitnessCenter("A002", 2024, 2, 45),
    FitnessCenter("A003", 2024, 3, 90),
    FitnessCenter("A004", 2024, 4, 30),
    FitnessCenter("A005", 2024, 10, 120),
    FitnessCenter("B006", 2025, 11, 60),
    FitnessCenter("B007", 2025, 5, 45),
    FitnessCenter("B008", 2025, 6, 90),
    FitnessCenter("B009", 2025, 7, 30),
    FitnessCenter("B010", 2025, 8, 120)
]

yearly_duration = {}
for session in fitness_sessions:
    if session.year in yearly_duration:
        yearly_duration[session.year] += session.duration
    else:
        yearly_duration[session.year] = session.duration
max_duration = max(yearly_duration.values())
max_years = [year for year, duration in yearly_duration.items() if duration == max_duration]
result_year = min(max_years)

print(f"Год с наибольшей суммарной продолжительностью занятий: {result_year}")
print(f"Суммарная продолжительность: {max_duration} мин.")