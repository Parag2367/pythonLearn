"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store cumulative sums and their counts
        d = {0: 1}
        sums = 0  # Cumulative sum
        count = 0  # Result counter

        # Iterate through the array
        for i in range(len(nums)):
            sums += nums[i]  # Update cumulative sum

            # If (current cumulative sum - k) exists in the dictionary, add its count to the result
            if sums - k in d:
                count += d[sums - k]

            # Update the dictionary with the current cumulative sum
            if sums in d:
                d[sums] += 1

            d[sums] = 1

        return count


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        total = 0
        prefix = {0: 1}

        for num in nums:
            curr += num
            diff = curr - k

            total += prefix.get(diff, 0)
            prefix[curr] = 1 + prefix.get(curr, 0)
        return total


s1 = Solution()
print(s1.subarraySum([3, 1, 3, 4, 3], 6))
