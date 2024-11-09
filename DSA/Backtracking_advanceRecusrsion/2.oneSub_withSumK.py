"""
one subsequence with sum = k 
"""


def one_subsum(nums: list, k):
    def backtrack(arr, index, total):
        if total > k:
            return

        if index >= len(nums):
            if total == k:
                result.append(arr.copy())
                return True
            return False

        arr.append(nums[index])
        total += nums[index]
        if backtrack(arr, index + 1, total):
            return True

        e = arr.pop()
        total -= e
        return backtrack(arr, index + 1, total)

    result = []
    backtrack([], 0, 0)
    return result


print(one_subsum([1, 2, 3, 7, 1, 3, 4], 5))
