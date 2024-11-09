"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.


Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)
        count = 0

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                if total > goal:
                    break

                if total == goal:
                    count += 1

        return count


class optimal:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def countSub(nums, goal):
            if goal < 0:
                return 0
            n = len(nums)
            count, left, right, sum = 0, 0, 0, 0

            while right < n:
                # sum as we have to keep it equal or less then goal
                sum += nums[right]
                # if sum > goal move left unless sum is <= goal
                while sum > goal:
                    sum -= nums[left]
                    left += 1
                # for counting number of sub array each time right goes ahead
                count += right - left + 1
                right += 1

            return count

        # nice logic:count of subarray <= goal - <= goal -1 == count of subarray = goal
        return countSub(nums, goal) - countSub(nums, goal - 1)
