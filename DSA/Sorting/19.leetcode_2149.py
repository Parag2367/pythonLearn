"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
"""

# class Solu:
#     """
#     TC: O(n) + O(n) = O(2n) == O(n)
#     SC: O(n)
#     """

#     def rearrange(self, nums):
#         n = len(nums)
#         positive = []
#         negative = []
#         # result = []
#         for a in nums:
#             if a > 0:
#                 positive.append(a)
#             else:
#                 negative.append(a)

#         for i in range(n):
#             if i % 2 == 0:
#                 nums[i] = positive[(i // 2)]

#             else:
#                 nums[i] = negative[(i // 2)]
#         # for i in range(n // 2):
#         #     result.append(positive[i])
#         #     result.append(negative[i])

#         print(nums)
#         # print(result)


# obj1 = Solu()
# obj1.rearrange([-3, 4, 1, -2, -5, 2, -4])


class Optimal:
    """
    TC: O(n)
    SC: O(n)
    """

    def result(self, nums):
        res = [0] * len(nums)
        i, j = 0, 1

        for k in range(len(nums)):
            if nums[k] > 0:
                res[i] = nums[k]
                i += 2

            else:
                res[j] = nums[k]
                j += 2

        return res


obj2 = Optimal()
print(obj2.result([-3, 4, 6, 1, -2, -5, 2, -4]))
