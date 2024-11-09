"""
Subset Sum
"""


def subset_sum(nums: list):
    def backtrack(arr, index):
        if index >= len(nums):
            result.append(sum(arr.copy()))
            return

        arr.append(nums[index])
        backtrack(arr, index + 1)
        arr.pop()
        backtrack(arr, index + 1)

    result = []
    backtrack([], 0)

    result.sort()
    return result


print(subset_sum([3, 1, 2]))


def optimal(nums: list):
    def backtrack(total, index):
        if index >= len(nums):
            result.append(total)
            return

        backtrack(total + nums[index], index + 1)
        backtrack(total, index + 1)

    result = []
    backtrack(0, 0)

    result.sort()
    return result


print(optimal([3, 1, 2]))
