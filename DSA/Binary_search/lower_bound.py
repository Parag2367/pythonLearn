"""
lower bound : it is the smallest index such that arr[mid] >= target
"""


def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


print(lower_bound([3, 4, 7, 8, 8, 10], 12))
