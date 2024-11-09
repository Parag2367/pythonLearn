# """
# Write a Python code to check whether the given string is symmetrical.
# Symmetrical string means First half of the string = Second half of the string or palindrome.
# """


# def sym(mystr: str):
#     n = len(mystr)
#     return mystr == mystr[::-1]


# print(sym("abca"))


# def is_palindrome(s, start, end):
#     while start <= end:
#         if s[start] != s[end]:
#             return False

#         start += 1
#         end -= 1

#     return True


# print(is_palindrome("abca", 0, 3))


# """
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# """


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# """
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.


# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
# """
# from typing import List


# class Solution1:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)
#         res, left, right = 0, 0, n - 1

#         while left < right:
#             if nums[left] + nums[right] == k:
#                 res += 1
#                 left += 1
#                 right -= 1

#             elif nums[left] + nums[right] < k:
#                 left += 1

#             else:
#                 right -= 1

#         return res


# """
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# """


# def maxarea(height: list):
#     max_area = 0
#     left = 0
#     right = len(height) - 1

#     while left < right:
#         # (right-left) == breadth, min(height[left], height[right]) == length
#         max_area = max(max_area, (right - left) * min(height[left], height[right]))

#         if height[left] < height[right]:
#             left += 1

#         else:
#             right -= 1

#     return max_area


# """
# Given an array nums of distinct integers, return all the possible
# permutations
# . You can return the answer in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
# """


# class Solution3:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         cur = []

#         def per(nums, cur):

#             if len(nums) == 0:
#                 ans.append(cur)

#             for i in range(len(nums)):
#                 per(nums[:i] + nums[i + 1 :], cur + nums[i : i + 1])

#         per(nums, cur)
#         return ans


# def permute(mystr: str) -> list:
#     ans = []
#     cur = ""

#     def per(mystr, cur):

#         if len(mystr) == 0:
#             ans.append(cur)

#         for i in range(len(mystr)):
#             per(mystr[:i] + mystr[i + 1 :], cur + mystr[i : i + 1])

#     per(mystr, cur)
#     return ans


# print(permute("abcd"))


# str1 = "visheshsahu"

# mydict = dict()
# mylist = []
# for char in str1:
#     mydict[char] = mydict.get(char, 0) + 1


# maxi = 0
# second_maxi = 0

# for a in mydict.values():
#     if a > maxi:
#         second_maxi = maxi
#         maxi = a

#     elif a > second_maxi and a != maxi:
#         second_maxi = a

#     else:
#         second_maxi = a

# # r = sorted(mydict.items(), key=lambda x: x[1])

# for k, v in mydict.items():
#     if v == second_maxi:
#         mylist.append(k)

# print(mydict)
# print(second_maxi)
# print(mylist, second_maxi)


"""
two sum for big list
"""


# def two_sum(mylist: list, target: int):
#     n = len(mylist)
#     mydict = dict()
#     result = []

#     for i in range(n):
#         remaining = target - mylist[i]

#         if remaining in mydict:
#             result.append([mylist[i], mylist[mydict[remaining]]])

#         mydict[mylist[i]] = i

#     return result


# print(two_sum([3, 4, 2, 5], 7))

"""
move zeroes to end
"""


# def move_zeroes(nums: list):

#     n = len(nums)
#     i = 0

#     while i < n:
#         if nums[i] == 0:
#             break

#         i += 1

#     j = i + 1

#     while j < n:
#         if nums[j] != 0:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1

#         j += 1

#     return nums


# print(move_zeroes([0]))


def continous(ip: list):
    i = 0
    maxi = 0
    count = 0
    for j in range(1, len(ip)):
        a = ip[j] - ip[i]
        if a == 1:
            count += 1
            i += 1
        else:
            i = j
            maxi = max(count, maxi)
            count = 0

    return max(maxi, count) + 1


print(continous([1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5, 6, 7]))
# [1, 2, 3, 2, 3, 4, 5, 6, 7, 1, 3, 5, 6, 7]


# this is for any succesive
def succesive(nums: list):
    myset = set()
    for a in nums:
        myset.add(a)

    longest = 0
    for a in myset:
        if a - 1 not in myset:
            x = a
            count = 1

            while x + 1 in myset:
                count += 1
                x += 1

            longest = max(longest, count)

    return longest


print(succesive([1, 2, 3, 2, 3, 4, 5, 6, 7, 1, 3, 5, 6, 7]))


"""
Subarray with largest sum and that subarray

[-2,1,-3,4,-1,2,1,-5,4]
"""


def max_sum(nums: list):
    sum = 0
    maxi = float("-inf")
    mylist = []

    for a in nums:
        sum += a

        if sum > maxi:
            maxi = sum
            mylist.append(a)
        else:
            mylist.pop()

        if sum < 0:
            sum = 0

    return maxi, mylist


print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
