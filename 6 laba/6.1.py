names = [
    "Алексей", "Борис", "Анна",
    "Дмитрий", "Алиса", "Сергей",
    "Артём", "Мария", "Андрей",
    "Елена", "Артур", "Алекс"
]

print("Имена, начинающиеся на 'А':")
for name in names:
    if name.startswith('А') or name.startswith('A'):
        print(name)