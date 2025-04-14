def con(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1, 2, 3, 4]
print(con(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(con(nums))

nums = [1, 2, 3, 1]
print(con(nums))
