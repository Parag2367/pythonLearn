"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


class Bruteforce:
    """
    Note that you must do this in-place without making a copy of the array.
    TC: O(n) as we are using three diff for loop
    SC: O(n) as new temp list
    """

    def removezeroes(self, arr):
        temp = []
        for a in arr:
            if a != 0:
                temp.append(a)

        for i in range(0, len(temp)):
            arr[i] = temp[i]  # doing this as we to do it in place

        for i in range(len(temp), len(arr)):
            arr[i] = 0
        print(arr)


obj1 = Bruteforce()
obj1.removezeroes([1, 0, 1])


class Optimal:
    """
    Note that you must do this in-place without making a copy of the array.
    Two pointer approach
    TC: O(n)
    SC: O(1)
    """

    def removezeroes(self, arr):
        if len(arr) == 1:
            return
        n = len(arr)
        i = 0
        while i < n:
            # first pointer, we will have to start it when the value is 0, so to find that we are using this
            if arr[i] == 0:
                break
            i += 1
        else:
            return
        # above while loop is only for finding first zero
        # second pointer: it should be one ahead of i
        j = i + 1
        while j < n:
            # if arr[j] is not equal to zero then only swap and incement i
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]  # doing this as we to do it in place
                i += 1
            j += 1
        print(arr)


obj2 = Optimal()
obj2.removezeroes([1, 0, 1])

# class SoluOptimal:
#     """
#     TC: O(n^2)
#     SC:
#     """

#     # if wqe try to use index in range we will get out of index error as array is changing, to avoid that we can store this array in a variable and use it,
#     # but question restriction is that we should not make any copy of the array
#     def removezeroes(self, arr: list):
#         cnt = 0
#         for a in arr:
#             if a == 0:
#                 arr.remove(a)
#                 cnt += 1
#         print(arr + [0] * cnt)


# obj1 = SoluOptimal()
# obj1.removezeroes([0, 1, 0, 3, 12, 1, 0])


# def test(nums):
#     n = len(nums)
#     i = 0
#     for i in range(0, n):
#         if nums[i] == 0:
#             break
#         else:
#             return

#     j = i + 1
#     while j < n:
#         if nums[j] != 0:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#         else:
#             j += 1
#     print(nums)


# test([0, 1, 0, 3, 12])
