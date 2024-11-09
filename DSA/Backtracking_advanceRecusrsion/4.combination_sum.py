"""
Combination sum , you can use any number any number of times
"""


def comb_sum(nums: list, target):
    def backtrack(arr, index, target):
        if target == 0:
            result.append(arr.copy())
            return

        if index >= len(nums):
            return

        if nums[index] <= target:
            arr.append(nums[index])
            target -= nums[index]
            backtrack(arr, index, target)
            e = arr.pop()
            target += e

        backtrack(arr, index + 1, target)

    result = []
    backtrack([], 0, target)

    return result


print(comb_sum([2, 3, 6, 7], 7))
