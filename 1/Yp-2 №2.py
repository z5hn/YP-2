def combinationSum2(candidates, target):
    candidates.sort()  # Сортируем
    result = []

    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):  # Пропускаем одинаковые элементы
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])  # Рекурсивный вызов

    backtrack(0, target, [])
    return result

candidates = [5, 5, 2, 1, 2]
target = 5
print(combinationSum2(candidates, target))

candidates = [10, 1, 2, 8, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
