sequence = list(map(int, input().split()))

first_positive = next((x for x in sequence if x > 0), None)

last_negative = next((x for x in reversed(sequence) if x < 0), None)

print(f"Первый положительный: {first_positive}")
print(f"Последний отрицательный: {last_negative}")
