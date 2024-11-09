"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

constraint = nums is either in 0,1,2
"""


class Solu:
    """
    TC: O(n) +O(n) + O(n)
    SC: O(n)
    """

    def sort_colurs(self, nums):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for a in nums:
            if a == 0:
                cnt0 += 1
            if a == 1:
                cnt1 += 1
            if a == 2:
                cnt2 += 1

        nums[:] = [0] * cnt0 + [1] * cnt1 + [2] * cnt2

        print(nums)


obj1 = Solu()
obj1.sort_colurs([2, 0, 2, 1, 1, 0])


class Optimal:
    """
    TC: O(n)
    SX: O(1)
    """

    def sort_colors(self, nums):
        # using Dutch National Flag algorithm
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        print(nums)


obj2 = Optimal()
obj2.sort_colors([0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 0])


# def test(nums):
#     l = 0
#     m = 0
#     h = len(nums) - 1

#     while m <= h:
#         if nums[m] == 0:
#             nums[l], nums[m] = nums[m], nums[l]
#             l += 1
#             m += 1

#         if nums[m] == 1:
#             m += 1

#         if nums[m] == 2:
#             nums[m], nums[h] = nums[h], nums[m]
#             h -= 1
