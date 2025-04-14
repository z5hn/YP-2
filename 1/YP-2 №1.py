def count_jewels(J, S):
    jewels = set(J)
    count = 0
    for char in S:
        if char in jewels:
            count += 1
    return count

J = input("Драгоценности:").strip()
S = input("Камни:").strip()
print(count_jewels(J, S))
