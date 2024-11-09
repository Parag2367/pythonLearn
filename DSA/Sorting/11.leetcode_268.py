"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""


# Brute force
class Solu:
    """
    TC: O(n^2)
    SC: O(1)
    """

    def missingnumbers(self, nums):
        for a in range(0, len(nums) + 1):
            if a not in nums:
                return a


# optimal (using sum of numbers)


class Optimal:
    """
    TC: O(n) for sum
    SC: O(1)
    """

    def missingnumbers(self, nums) -> int:
        n = len(nums)
        original_total = (n * (n + 1)) // 2  # formula for sum of natural numbers
        return original_total - sum(nums)  # this will give us the missing number


obj1 = Optimal()
print(obj1.missingnumbers([1, 2, 3, 2]))
