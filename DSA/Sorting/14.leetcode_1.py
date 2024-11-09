"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


# Brute force
class Solu:
    """
    TC: O(n^2)
    SC: O(1)
    """

    def twosum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])

        # for i in range(len(nums) - 1):
        #     temp = target - nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == temp:
        #             print([i, j])


obj2 = Solu()
obj2.twosum([3, 2, 3], 6)


# optimal


class Optimal:
    def twosum(self, nums, target):
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i


obj1 = Optimal()
print(obj1.twosum([2, 7, 11, 15], 17))


# def test(nums, target):
#     hash_map = dict()
#     n = len(nums)
#     for i in range(n):
#         remaining = target - nums[i]
#         if remaining in hash_map.items():
#             return (hash_map[remaining], i)

#         hash_map[nums[i]] = i
