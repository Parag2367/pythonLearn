"""
There is an integer array ‘A’ of size ‘N’.

A sequence is successive when the adjacent elements of the sequence have a difference of 1.

You must return the length of the longest successive sequence.

Note:

You can reorder the array to form a sequence. 
For example,

Input:
A = [5, 8, 3, 2, 1, 4], N = 6
Output:
5
Explanation: 
The resultant sequence can be 1, 2, 3, 4, 5.    
The length of the sequence is 5.
"""

# class Solu:
#     def succesive(self, nums):
#         nums.sort()
#         i = 0
#         while i < len(nums) - 1:
#             if (nums[i + 1] - nums[i]) != 1:
#                 break
#             i += 1

#         print(i + 1)


# obj1 = Solu()
# obj1.succesive([1, 8, 3, 2, 1, 4])


class Optimal:
    def succesive(self, nums):
        myset = set()
        for num in nums:
            myset.add(num)

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


obj2 = Optimal()
print(obj2.succesive([2, 3, 2, 2, 101, 102, 99, 87, 100, 5, 103]))
