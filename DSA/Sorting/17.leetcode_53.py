"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
"""


class Optimal:
    """
    Using Kadane's Algorithm
    TC: O(n)
    SC: O(1)
    """

    def maximum(self, nums):
        maxi = float("-inf")
        n = len(nums)
        sum = 0

        for i in range(n):
            # this should go on as we have to find maximum subarray
            sum = sum + nums[i]
            # this is to store sum into a maximum value
            if sum > maxi:
                maxi = sum
            # case if sum < 0, make it zero and go ahead
            if sum < 0:
                sum = 0

        return maxi


obj1 = Optimal()
print(obj1.maximum([5, 4, -1, 7, 8]))


# def test(nums):
#     maxi = float("-inf")
#     sum = 0

#     for i in range(len(nums)):
#         sum = sum + nums[i]

#         if sum > maxi:
#             maxi = sum

#         if sum < 0:
#             sum = 0
