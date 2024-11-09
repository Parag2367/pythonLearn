"""
Backtracking: very important , it is similar to permutations
It gives us all the possible sub-arrays (continous /non-continous)

In earlier code we were using sliding window approach for getting continous subarrays
"""

ans = []


def subset(arr, index):
    if index >= n:
        ans.append(arr.copy())
        return
    arr.append(nums[index])
    subset(arr, index + 1)
    arr.pop()
    subset(arr, index + 1)

    return ans


nums = [1, 2, 2]
# nums = [55, 43, 91]
# nums = ["w", "y", "u", "f", "u", "v", "n", "e"]
n = len(nums)
a = subset([], 0)
print(a)

from typing import List


class Solution:
    def subsets(self, nums: List[int]):
        ans = []
        n = len(nums)

        def sub(arr, index):
            if index >= n:
                ans.append(arr.copy())
                return
            arr.append(nums[index])
            sub(arr, index + 1)
            arr.pop()
            sub(arr, index + 1)
            return ans

        a = sub([], 0)
        return a
