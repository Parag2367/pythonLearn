"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


class Brute:
    def search(self, nums, target):
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                else:
                    last = i

        return [first, last]


class Optimal:
    def searching(self, nums, target):
        def binary(nums, target, searching_left):
            n = len(nums)
            ind = -1
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ind = mid
                    # doing this suppose if we got the target but still we will have to check left side for the first occurence
                    if searching_left:
                        high = mid - 1
                    else:
                        # doing this suppose if we got the target but still we will have to check right side for the last occurence
                        low = mid + 1

                elif nums[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

            return ind

        left = binary(nums, target, True)
        if left == -1:
            return [-1, -1]
        right = binary(nums, target, False)

        return [left, right]


obj1 = Optimal()
print(obj1.searching([2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19], 10))


class Sol:
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ind = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ind = mid
                high = mid - 1

            else:
                ind = mid
                low = mid + 1

        return [low, mid]


obj2 = Sol()
print(obj2.search([2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19], 10))
