class Binary:  # applies only on sorted array
    def bin_search(self, nums: list, a):
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == a:
                return mid

            elif nums[mid] > a:
                high = mid - 1

            else:
                low = mid + 1
        return mid


"""
lower bound : means target >= nums[mid] : it will give the start index of that number
"""


def lower(nums: list, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


"""
higher bound: target > nums[mid] : it will always give index just above the target number's index
"""


def higher(nums: list, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ans = mid
            high = mid - 1

        else:
            low = mid = 1

    return ans


"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 
"""
# upper bound


def index(nums: list, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


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


def start_end(nums: list, target):
    def search(nums, target, check_left):
        n = len(nums)
        low = 0
        high = n - 1
        ind = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ind = mid

                if check_left:
                    high = mid - 1

                else:
                    low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return ind

    left_part = search(nums, target, True)
    if (
        left_part == -1
    ):  # this is if there is no target in array, it will return ind as it is
        return [-1, -1]
    right_part = search(nums, target, False)

    return (left_part, right_part)


"""
Problem statement
You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.



Find the total number of occurrences of 'x' in the array/list.



Example:
Input: 'n' = 7, 'x' = 3
'arr' = [1, 1, 1, 2, 2, 3, 3]

Output: 2

Explanation: Total occurrences of '3' in the array 'arr' is 2.
"""


def search(nums, target):
    def bin(nums, target, search_left):
        n = len(nums)
        low = 0
        high = n - 1
        ind = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ind = mid

                if search_left:
                    high = mid - 1

                else:
                    low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return ind

    left = bin(nums, target, True)
    if left == -1:
        return -1
    right = bin(nums, target, False)

    return right - left + 1


"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""


def rot_unique(nums: list, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # for sorted part
        if nums[low] <= nums[mid]:
            if nums[low] < target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:  # for unsorted part
            if nums[mid] < target <= nums[high]:
                low = mid + 1

            else:
                high = mid - 1

    return -1


"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""


def rot_nonunique(nums: list, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] == nums[mid] == nums[high]:
            high -= 1
            low += 1
        if nums[low] <= nums[mid]:  # sorted part

            if nums[low] <= target <= nums[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1

            else:
                high = mid - 1

    return -1


"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""


class Solution1:
    def miniarray(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        mini = float("inf")

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[mid]:
                mini = min(mini, nums[low])
                low = mid + 1

            else:
                mini = min(mini, nums[mid])
                high = mid - 1

        return mini


"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


def peak(nums: list):
    n = len(nums)

    if n == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[-1] > nums[-2]:
        return n - 1

    low = 1  # why because we have to check for after first
    high = n - 2  # why because we have to check for before last

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid

        elif nums[mid] > nums[mid + 1]:
            # in this we are check if there is any peak before mid
            high = mid - 1

        else:
            # in this we are check if there is any peak after mid
            low = mid + 1


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


def single(nums: list):
    n = len(nums)

    if len(nums) == 0:
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


"""
Problem statement
You are given a positive integer ‘n’.



Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).



Example:
Input: ‘n’ = 7

Output: 2

Explanation:
The square root of the number 7 lies between 2 and 3, so the floor value is 2.
"""


def root(n):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            low = mid + 1

        else:
            high = mid - 1

    return high


"""
Problem statement
You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 'm(1/n)'. If the 'nth root is not an integer, return -1.



Note:
'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


Example:
Input: ‘n’ = 3, ‘m’ = 27

Output: 3

Explanation: 
3rd Root of 27 is 3, as (3)^3 equals 27.
"""


def mthroot(m, n):
    low = 1
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if mid**m == n:
            return mid

        if mid**m > n:
            high = mid - 1

        else:
            low = mid + 1
    return -1


"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""


def findmin(nums):
    n = len(nums)
    low = 0
    high = n - 1
    mini = float("inf")

    while low <= high:
        mid = (low + high) // 2

        # no rotation happend
        if nums[low] <= nums[high]:
            mini = min(mini, nums[low])
            break

        # if rotation for the sorted part

        if nums[low] <= nums[mid]:
            mini = min(mini, nums[low])
            low = mid + 1

        else:
            mini = min(mini, nums[mid])
            high = mid - 1

    return mini


"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""
import math


class Solution:
    def total_hours(self, piles: list, k: int):
        total = 0

        for i in range(len(piles)):
            total += math.ceil(piles[i] / k)

        return total

    def brute(self, piles, hour):
        m = max(piles)
        total_time = 0

        for i in range(m + 1):
            total_time = self.total_hours(piles, i)

            if total_time <= hour:
                return i

    def optimal(self, piles, hour):
        m = max(piles)
        low = 1
        high = m
        ans = 1

        while low <= high:
            mid = (low + high) // 2

            total_time = self.total_hours(piles, mid)

            if total_time <= hour:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans
