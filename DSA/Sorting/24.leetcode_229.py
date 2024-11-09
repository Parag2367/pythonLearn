"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]):
        n = len(nums)
        mydict = dict()
        result = []
        for a in nums:
            mydict[a] = mydict.get(a, 0) + 1

        for k, v in mydict.items():
            if v > n / 3:
                result.append(k)

        return result


obj1 = Solution()

print(obj1.majorityElement([3, 2, 3]))


def major(nums: list):
    n = len(nums)
    cand1 = nums[0]
    c1 = 0
    cand2 = nums[1]
    c2 = 0

    for j in range(n):
        if nums[j] == cand1:
            c1 += 1

        elif nums[j] == cand2:
            c2 += 1

        else:
            c1 -= 1
            c2 -= 1

        if c1 == 0:
            cand1 = nums[j]
            c1 = 1
        if c2 == 0:
            cand2 = nums[j]
            c2 = 1

    if c1 > c2:
        return cand1
    else:
        return cand2


print(major([1, 2, 1, 2, 1, 2, 1, 2, 3, 1, 2, 2]))
