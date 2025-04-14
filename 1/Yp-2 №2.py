def comb(candidates, target):
    candidates.sort()
    result = []

    def back(start, target, path):
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            back(i + 1, target - candidates[i], path + [candidates[i]])

    back(0, target, [])
    return result


candidates = [5, 5, 2, 1,3]
target = 5
print(comb(candidates, target))

candidates = [10, 1, 8, 7, 6, 1, 5]
target = 8
print(comb(candidates, target))
