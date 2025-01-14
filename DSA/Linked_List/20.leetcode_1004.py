"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


class Solution:
    # Better
    """
    TC: O(2n)
    SC: O(1)
    """

    def consecutiveOnes(self, nums, k):
        n = len(nums)
        max_length, left, right = 0, 0, 0
        zeroes = 0

        while right < n:
            if nums[right] == 0:
                zeroes += 1
            # condition to move left forward to make sure zeroes are equal to k
            while zeroes > k:  # due to this it will traverse n times more
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            if zeroes <= k:
                length = right - left + 1
                max_length = max(max_length, length)

            right += 1

        return max_length


obj1 = Solution()
print(
    obj1.consecutiveOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
)


class Solu:
    """
    TC: O(n)
    SC: O(1)
    """

    def consecutiveOnes(self, nums, k):
        n = len(nums)
        zeroes, max_length, left, right = 0, 0, 0, 0

        while right < n:
            if nums[right] == 0:
                zeroes += 1

            if zeroes > k:  # due to this only one iteration
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            if zeroes <= k:
                length = right - left + 1
                max_length = max(max_length, length)

            right += 1

        return max_length


obj1 = Solu()
print(
    obj1.consecutiveOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
)
