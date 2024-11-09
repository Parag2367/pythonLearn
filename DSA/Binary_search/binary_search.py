"""

"""

nums = [2, 3, 4, 6, 8, 9]
target = 3


def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return


def bin(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return
