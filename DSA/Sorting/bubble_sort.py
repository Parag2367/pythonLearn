"""
Bubble sort

TC: Worst and Avg case = O(n^2), Best case (when it is sorted)= O(n)
SC: O(1)

"""


def bubble_sort(arr: list):
    n = len(arr)

    # we have to go till second last element as we interchange position so second_last will change from last, that is why last is not needed in range

    # traveresing in reverse order as it is just for moving, we can also move in normal order (1,n) then j will be (0 ,n-i)
    # we will always traverse n-1 times
    for i in range(n - 1, 0, -1):
        # it will compare till ith index
        for j in range(0, i):
            # comparing higher amaong two adjacent and swapping position
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [13, 46, 24, 52, 20, 9]
print(bubble_sort(arr))


def bubble(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr1 = [13, 46, 24, 52, 20, 9]
bubble(arr1)
print(arr1)


def bubble_sort_p(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bub(nums: list):
    n = len(nums)

    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
