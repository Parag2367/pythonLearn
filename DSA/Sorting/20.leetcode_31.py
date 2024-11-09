"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
"""


class Solu:
    def next_per(self, nums):
        n = len(nums)
        ind = -1

        # for finding breakpoint , so that we will have two parts
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        # case where no breakpoint is found or last permutation or largest possible number , so the answer will be reverse of it
        if ind == -1:
            nums.reverse()
            return

        # for finding next per, the number at break point is compared to remainn right half, to check for first larger number then it
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        # reversing the numbers to get the next permutation
        nums[ind + 1 :] = reversed(nums[ind + 1 :])

        return nums


obj1 = Solu()
print(obj1.next_per([2, 1, 5, 4, 3, 0, 0]))
