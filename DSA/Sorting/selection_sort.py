"""
Selection sort

TC : O(n2)
SC: O(1)
"""


def selection_sort(arr: list):
    n = len(arr)
    # traversing the array whole
    for i in range(0, n):
        min = i  # minimum index is i
        # traversing remaining array not first element as we are comparing first with rest
        for j in range(i + 1, n):
            if (
                arr[j] < arr[min]
            ):  # checking if there is a minimum value in remaianing array
                min = j
        # interchanging position of first with minimum in the array
        arr[i], arr[min] = arr[min], arr[i]  # posible in list as it is mutable
    print(arr)


arr = [64, 25, 12, 22, 11]
selection_sort(arr)


def selection(arr):
    n = len(arr)

    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


def selection_sort_p(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


def selection_sort2(nums: list):
    n = len(nums)
    for i in range(0, n):
        min = nums[i]
        for j in range(i + 1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
