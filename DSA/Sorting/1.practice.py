"""
Given an array ‘arr’ of size ‘n’ find the largest element in the array.
Example:
Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
Output: 5
Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.

"""


# brite-force:
def largest(arr):
    arr.sort()
    return arr[-1]


print(largest([1, 2, 3, 4, 5]))

# optimal
# def largest(num: int, arr: list):
#     max = float("-inf")

#     for a in arr:
#         if a > max:
#             max = a
#     print(f"largest element in {arr} is {max}")


# largest(5, [1, 2, 3, 4, 5])


# optimal using merge sort:
# def largest_optimal(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2

#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     left_half = largest_optimal(left_half)
#     right_half = largest_optimal(right_half)

#     return merge(left_half, right_half)


# def merge(left, right):

#     merged = []
#     i, j = 0, 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i += 1

#         else:
#             merged.append(right[j])
#             j += 1

#     while i < len(left):
#         merged.append(left[i])
#         i += 1

#     while j < len(right):
#         merged.append(right[j])
#         j += 1

#     return merged


# sorted = largest_optimal([1, 2, 3, 4, 5])
# print(f"largest element is {sorted} is {sorted[-1]}")
