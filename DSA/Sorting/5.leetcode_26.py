"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


# brite force:
class BruteSol:
    def removeDup(self, arr):
        my_dict = dict()
        for a in arr:
            my_dict[a] = 0

        # dictionary always gives us unique value of keys as keys cannot be repaeated
        j = 0
        for a in my_dict:
            arr[j] = a
            j += 1

        return (
            j + 1
        )  # as we have started from zero, so this will give us the number of unique elements


# optimal way
# two pointer
class Solution:
    def removeDuplicate(self, arr: list):
        i = 0
        # i will start from zero, j will start from one position ahead of i
        for j in range(1, len(arr)):
            # it will check if arr[i] != arr[j], i will move ahead,
            # arr[i] = arr[j] doing this as we have to travesrse whole array and maintain the original position
            if arr[i] != arr[j]:
                i += 1
                # by doing this , as we are looping through using j so this will make sure if will compare each element
                arr[i] = arr[j]
        # returning number of unique , as i starts from zero tha is why +1
        print(arr)
        return i + 1


obj1 = Solution()
print(obj1.removeDuplicate([2, 2, 2, 3, 3, 4, 5, 6]))


# class psolu:
#     def remove(self, nums):
#         i = 0

#         for j in range(1, len(nums)):
#             if nums[i] != nums[j]:
#                 i += 1
#                 nums[i] = nums[j]
#         print(nums)
#         return i + 1


def test(nums):
    n = len(nums)
    i = 0
    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    count = i + 1
    print(nums[:count])


test([1, 1, 2, 2])


def rem(nums: list):
    i = 0
    n = len(nums)

    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
