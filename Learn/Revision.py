# """Leap year"""


# def leap_year(year: int) -> bool:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False


# print(leap_year(120))

# """
# Write a Python function that takes a number as a parameter and checks
# whether the number is prime or not.
# """


# def prime(nums: int) -> bool:
#     cnt = 0
#     for i in range(1, nums):
#         if nums % i == 0:
#             cnt += 1
#     if cnt > 1:
#         return False
#     else:
#         return True


# print(prime(3))


# """Calculate factorial of a number entered by user."""


# def fact(num: int) -> int:
#     i = num
#     fact = 1
#     while i >= 1:
#         fact = fact * i
#         i -= 1

#     return fact


# print(fact(5))


# """
# Create a function addDigits() that takes an integer as an argument.
# Calculate the sum of digits of that number.
# addDigits(123)
# 6
# """


# def addDigits(num: int) -> int:
#     a = num
#     total = 0

#     while a > 0:
#         total = total + a % 10
#         a = a // 10

#     return total


# print(addDigits(234))


# """
# Generate a list of list using list comprehension where format should
# be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]]
# """


# def comp(num: int) -> list:

#     mylist = [[i, "even"] if i % 2 == 0 else [i, "odd"] for i in range(1, num)]
#     return mylist


# print(comp(22))


# """
# armstrong
# """


# def arm(num: int) -> bool:
#     a = num
#     total = 0

#     while a > 0:
#         last_digit = a % 10
#         total = total + (last_digit**3)
#         a = a // 10

#     return total == num


# print(arm(123))


# """
# Find largest number in a list
# """


# def large(mylist: list) -> float:
#     largest = float("-inf")

#     for a in mylist:
#         if a > largest:
#             largest = a

#     return largest


# print(large([23, 45, 67, 88, 99, 22]))


# """
# Write a Python code to find the occurrence of each element in a list
# and print the element with the highest occurrence.

# """


# def occur(my_list: list) -> dict:
#     new_list = []
#     for a in my_list:
#         if a not in new_list:
#             new_list.append(a)

#     occurence = 0
#     element = 0
#     for a in new_list:
#         cnt = my_list.count(a)
#         if cnt > occurence:
#             occurence = cnt
#             element = a

#     return {element: occurence}


# print(occur([23, 34, 56, 76, 56.655, 56, 34, 23, 34, 56, 56, 23]))


# # two colours/ dutch national flag


# def two_colours(nums):
#     low = 0
#     mid = 0
#     high = len(nums) - 1

#     while mid <= high:

#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             mid += 1
#             low += 1

#         if nums[mid] == 1:
#             mid += 1

#         if nums[mid] == 2:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1

#     return nums


"""
Reverse a integer/ checking for palindrome
"""


# class Solution:
#     def rev(self, num: int) -> int:
#         x = num
#         a = 0

#         while x > 0:
#             last_digit = x % 10
#             a = a * 10 + last_digit
#             x = x // 10

#         return a


# y = Solution()
# print(y.rev(234))


"""
Merge Sort
"""


def merge_sort(arr):
    # condition to stop recursion
    if len(arr) <= 1:
        return arr

    # dividing array in two part
    mid = len(arr) // 2

    # two prts of array
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursion on left and right parts
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # calling for merge when the recursion is stopped
    return merge(left_half, right_half)


# merge function to merge the array in sorted way, or sort is happened using this function
def merge(left, right):
    merged = []
    i, j = 0, 0

    # condition to check when niether i or j is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1
    # these below condition will only work once above while is false , which means eith i >= len(left) or j >= len(right)

    # condition to append the array if j is exhausted or j is out of index
    # happens when len(right) is smaller then len(left)
    while i < len(left):
        merged.append(left[i])
        i = i + 1

    # condition to check if i is exhausted or i is out of index
    # happens when len(right) is greater is len(left)
    while j < len(right):
        merged.append(right[j])
        j = j + 1

    return merged


# print(merge_sort([2, 2, 0, 0, 1, 1]))
# def merge_sort(nums: list):
#     n = len(nums)
#     if len(nums) <= 1:
#         return nums

#     left_part = nums[: n // 2]
#     right_part = nums[n // 2 :]

#     left_part = merge_sort(left_part)
#     right_part = merge_sort(right_part)

#     return merge(left_part, right_part)


# def merge(left: list, right: list):
#     i = 0
#     j = 0
#     merged = []

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i += 1

#         else:
#             merged.append(right[j])
#             j += 1

#     while i < len(left):
#         merged.append(left[i])

#     while j < len(right):
#         merged.append(right[j])

#     return merged


print(merge_sort([2, 2, 0, 0, 1, 1]))

# def merge_sort(nums: list):
#     if len(nums) <= 1:
#         return nums

#     mid = len(nums) // 2

#     left_part = nums[:mid]
#     right_part = nums[mid:]

#     left = merge_sort(left_part)
#     right = merge_sort(right_part)

#     return merge(left, right)


# def merge(left, right):
#     i = 0
#     j = 0
#     merged = []

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i += 1

#         else:
#             merged.append(right[j])
#             j += 1

#     while i < len(left):
#         merged.append(left[i])

#     while j < len(right):
#         merged.append(right[j])

#     return merged


"""
Quick sort
"""


# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high

#     while arr[i] <= pivot and i <= high - 1:
#         i += 1

#     while arr[j] > pivot and j > low + 1:
#         j -= 1

#     if i < j:
#         arr[i], arr[j] = arr[j], arr[i]

#     return j


# def quick_sort(arr, low, high):
#     if low < high:
#         p_index = partition(arr, low, high)
#         quick_sort(arr, low, p_index - 1)
#         quick_sort(arr, p_index + 1, high)
