"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""


class Solu:
    """
    TC: O(n)
    SC: O(1)
    """

    def consecutive(self, nums) -> int:
        count = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:  # case when consecutive number is not one
                maxi = max(
                    count, maxi
                )  # it will over write maxi very important step, this will give us count of 1s
                count = 0  # it will reset count to zero so that if we have another consecutive ones it will start from zero

        return max(count, maxi)  # return max of count or maxi


obj1 = Solu()
print(obj1.consecutive([1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]))


# def test(nums):
#     count = 0
#     maxi = 0

#     for a in nums:
#         if a == 1:
#             count += 1

#         else:
#             maxi = max(count, maxi)
#             count = 0

#     return max(maxi, count)
