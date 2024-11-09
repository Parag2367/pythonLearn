"""
Insertion sort

TC: WorstCase and Avg Case = O(n^2), Best case = O(n)
SC: O(1)

"""


def insertion_sort(arr):
    n = len(arr)

    # starting from 1 as 0 index element subarray cannot be compared as there will be only one element
    for i in range(1, n):
        # key equals to arr[i] this will make sure when we change the number the old number is stored in a variable
        key = arr[i]
        j = i - 1
        # j will always start from one less of i, and arr[j] should be greater then key then only we can sort otherwise no need of sorting

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # this is used to change the number
            j = j - 1
        # this will make sure when we change the number to a larger number the original number is stored back to its palce
        arr[j + 1] = key


arr = [14, 9, 15, 12, 6, 8, 13]

insertion_sort(arr)
print(arr)


def insertion(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        for j in range(i, -1, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key


insertion(arr)
print(arr)

# while j >= 0 and arr[j] > key:
#     arr[j + 1] = arr[j]
#     j = j - 1

# arr[j + 1] = key


def pract(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key


def ins(nums: list):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
