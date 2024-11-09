"""
Check if array is sorted and rotated
Time complexity = O(N) where N is the number of elements in list
Because we looping through the array only once

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
Space complexity = O(1)

"""

from typing import List


class Solution:

    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # We will count the rotations, we know the array can rotated only 1 time
        # and can be sorted, if the rotation will be greater than 1, we know the
        # array is not sorted and this return false
        rotations = 0
        for i in range(0, len(nums)):  # eg: [7,9,10,6,9]
            if nums[i] > nums[(i + 1) % n]:
                rotations += 1
            if rotations > 1:
                return False
        return True


arr1 = [3, 4, 5, 1, 2]
arr2 = [2, 1, 3, 4]

obj1 = Solution()
print(obj1.check(arr2))


class Solu:
    def rotate(self, nums):
        rotate = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotate += 1
            if rotate > 1:
                return False
        return True
