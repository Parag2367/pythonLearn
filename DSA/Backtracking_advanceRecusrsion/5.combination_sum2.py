"""
40. Combination Sum II, it should not have same combination
"""


def comb_sum2(nums, target):
    nums.sort()

    def backtrack(arr, index, target):
        if target == 0:
            result.append(arr.copy())
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            arr.append(nums[i])
            backtrack(arr, i + 1, target - nums[i])
            arr.pop()

    result = []
    backtrack([], 0, target)

    return result


print(comb_sum2([1, 1, 1, 2, 2], 4))
