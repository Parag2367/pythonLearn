"""
Given an array 'arr' containing 'n' elements, rotate this array left once and return it.
Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.
Example:
Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation: We moved the 2nd element to the 1st position, and 3rd element to the 2nd position, and 4th element to the 3rd position, and the 5th element to the 4th position, and move the 1st element to the 5th position.
"""

"""
TC: O(n) as it is using for loop which is checking every element in that array
SC: O(1)
"""


class Solu:
    def rotate(self, num: int, arr: list) -> list:
        temp = arr[0]
        for i in range(0, num - 1):
            arr[i] = arr[i + 1]
        arr[-1] = temp

        return arr


obj1 = Solu()
print(obj1.rotate(5, [1, 2, 3, 4, 5]))


# def rotate(nums):
#     temp = nums[0]
#     for i in range(0, len(nums)):
#         nums[i] = nums[i + 1]

#     nums[-1] = temp
#     return nums
