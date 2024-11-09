"""
You are given an array 'a' of size 'n' and an integer 'k'.

Find the length of the longest subarray of 'a' whose sum is equal to 'k'.
Example :
Input: ‘n’ = 7 ‘k’ = 3
‘a’ = [1, 2, 3, 1, 1, 1, 1]

Output: 3

Explanation: Subarrays whose sum = ‘3’ are:

[1, 2], [3], [1, 1, 1] and [1, 1, 1]

Here, the length of the longest subarray is 3, which is our final answer.
"""

# class Optimal:
#     """
#     TC: O(2n) = O(n)
#     SC: O(1)
#     """

#     def longestsub(self, nums: list, k: int):
#         n = len(nums)
#         L, R = 0, 0
#         max_length = 0
#         sum = nums[0]

#         while R < len(nums):
#             while L <= R and sum > k:
#                 sum = sum - nums[L]
#                 L += 1

#             if sum == k:
#                 max_length = max(max_length, L - R + 1)
#                 R += 1
#             if R < len(nums):
#                 sum += nums[R]
#             R += 1

#         return max_length


def test(nums, total):
    n = len(nums)
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum = sum + nums[k]
            if sum == total:
                max_length = max(max_length, j - i + 1)

    return max_length


# a = Optimal()
# print(a.longestsub([1, 2, 3, 1, 1, 1, 1], 3))

print(test([1, 2, 3, 1, 1, 1, 1], 3))
