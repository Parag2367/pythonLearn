"""
count of subsequence whose sum = k
"""


def count_sub(nums, k):
    def backtrack(arr, index, total):
        if total > k:
            return

        if index >= len(nums):
            if total == k:
                return 1
            return 0

        arr.append(nums[index])
        total += nums[index]
        pick = backtrack(arr, index + 1, total)

        e = arr.pop()
        total -= e
        unpick = backtrack(arr, index + 1, total)

        return pick + unpick

    count = backtrack([], 0, 0)
    print(count)
