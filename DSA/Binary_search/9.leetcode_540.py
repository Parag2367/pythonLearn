"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]):
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low = 1
        high = n - 2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                if mid % 2 == 1:
                    low = mid + 1
                else:
                    high = mid - 1
