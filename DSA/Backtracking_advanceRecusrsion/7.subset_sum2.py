"""
subset sum II
"""


def subset_sumII(nums: list):
    def backtrack(arr, index):
        nums.sort()

        result.append(arr.copy())

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            arr.append(nums[i])
            backtrack(arr, i + 1)
            arr.pop()

    result = []
    backtrack([], 0)

    return result


print(subset_sumII([4, 4, 4, 1, 4]))
