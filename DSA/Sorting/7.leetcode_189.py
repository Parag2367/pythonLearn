"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

# Better Solution
# class Solu:
#     """
#     TC =O(n)
#     SC = O(n) = O(n-k) + O(k) as slicing takes extra space
#     """

#     def rotatearr(self, arr: list, k: int):
#         n = len(arr)
#         k = k % n  # to optimize if k is greater then n , if k = n+1
#         # return arr[-k:] + arr[:-k] # this will be in new address location , but we have to make changes in the same list so following we can do
#         # arr[:] will make sure that same list is changed
#         arr[:] = arr[-k:] + arr[:-k]


# obj1 = Solu()
# print(obj1.rotatearr([-1, -100, 3, 99], 2))


# Optimal Solution:


class OptimalSolu:

    def rotate(self, arr, k: int):

        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]

                l = l + 1
                r = r - 1

        n = len(arr)
        k = k % n

        reverse(0, n - 1)
        reverse(0, n - k)
        reverse(n - k, n - 1)

        print(arr)


obj2 = OptimalSolu()
obj2.rotate([-1, -100, 3, 99], 2)


def better(nums, k):
    n = len(nums)
    k = k % n

    nums[:] = nums[-k:] + nums[:-k]
