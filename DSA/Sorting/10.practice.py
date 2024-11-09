"""
Problem statement
Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.

The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.

Note: 'a' and 'b' may contain duplicate elements, but the union array must contain unique elements.

Example:
Input: ‘n’ = 5 ‘m’ = 3
‘a’ = [1, 2, 3, 4, 6]
‘b’ = [2, 3, 5]

Output: [1, 2, 3, 4, 5, 6]
"""


class Solu:
    """
    TC: O(n) for loop * O(len(arr1))
    """

    def union(self, arr1, arr2):

        for a in arr2:
            if a not in arr1:
                arr1.append(a)

        print(arr1.sort())


obj1 = Solu()
obj1.union([1, 2, 3, 4, 5, 6], [2, 3, 5])


class optimal:
    """
    TC:O(n+m) as traversing both the arrays
    Sc: it seems O(n+m) but it will be O(1) because result will be our result so we are not storing
    """

    def unionofarray(self, arr1, arr2):
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if (
                    len(result) == 0 or result[-1] != arr1[i]
                ):  # added result[-1] this to make sure to only add number once if there is duplicate of it in another list and len(result) == 0 if result is empty
                    result.append(arr1[i])
                i += 1

            else:
                if (
                    len(result) == 0 or result[-1] != arr2[j]
                ):  # added this to make sure to only add number once if there is duplicate of it in another list
                    result.append(arr2[j])
                j += 1

        while i < len(arr1):
            if (
                len(result) == 0 or result[-1] != arr1[i]
            ):  # added this to make sure to only add number once if there is duplicate of it in another list
                result.append(arr1[i])
            i = i + 1

        while j < len(arr2):
            if (
                len(result) == 0 or result[-1] != arr2[j]
            ):  # added this to make sure to only add number once if there is duplicate of it in another list
                result.append(arr2[j])
            j = j + 1

        return list(result)


obj2 = optimal()
print(obj2.unionofarray([1, 2, 3, 4, 5, 6], [2, 3, 56]))


# def test(nums):

#     result = []
#     i, j = 0, 0
#     n = len(nums)

#     while i < n and j < n:
#         if nums[i] < nums[j]:
#             if len(result) == 0 or result[-1] != nums[i]:
#                 result.append(nums[i])
#             i += 1

#         else:
#             if len(result) == 0 or result[-1] != nums[j]:
#                 result.append(nums[j])
#             j += 1

#     while i < n:
#         if len(result) == 0 or result[-1] != nums[i]:
#             result.append(nums[i])
#         i += 1

#     while j < n:
#         if len(result) == 0 or result[-1] != nums[j]:
#             result.append(nums[j])
#         j += 1

#     print(result)
