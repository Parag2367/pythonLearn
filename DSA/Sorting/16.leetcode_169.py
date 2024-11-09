"""
Majority element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
"""


# better solution
class Solu:
    def majority(self, nums):
        """
        TC: O(n) +O(n) = O(n)
        SC: O(n)
        """
        mydict = {}
        for a in nums:
            mydict[a] = mydict.get(a, 0) + 1
        for k, v in mydict.items():
            if v > (len(nums) / 2):
                print(k)


obj1 = Solu()
obj1.majority([2, 2, 1, 1, 1, 2, 2])


class Optimal:
    """
        The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
        Mooree's voting algorithm
        TC: O(n)
        SC: O(1)
    """

    def majority(self, nums):
        candidate = nums[0]
        count = 0

        for i in range(len(nums)):
            if nums[i] == candidate:
                count += 1

            else:
                count -= 1

            if (
                count == 0
            ):  # this takes care of when count gets 0 but the number againg is there see below array
                candidate = nums[i]
                count = 1  # very important

        return candidate


obj2 = Optimal()
print(obj2.majority([2, 2, 2, 3, 4, 5, 6, 2, 2]))


# def test(nums):
#     cand = nums[0]
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] == cand:
#             count += 1
#         else:
#             count -= 1

#         if count == 0:  # when count gets zero while reducing
#             cand = nums[i]
#             count = 1

#     return cand
