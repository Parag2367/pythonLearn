"""
Right rotating an array means shifting the element at 'ith' index to (‘i+1') mod 'n' index, for all 'i' from 0 to ‘n-1'.



Example:
Input: 'n' = 5 , ‘arr’ = [3, 4, 5, 1, 2]

Output: 3 

Explanation:
If we rotate the array [1 ,2, 3, 4, 5] right '3' times then we will get the 'arr'. Thus 'r' = 3.
"""


class Solu:
    def findmin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        mini = float("inf")
        index = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]:
                if nums[low] < mini:
                    mini = nums[low]
                    index = low
                    break

            if nums[low] <= nums[mid]:
                if nums[low] < mini:
                    mini = nums[low]
                    index = low
                low = mid + 1

            else:
                if nums[mid] < mini:
                    mini = nums[mid]
                    index = mid
                high = mid - 1

        return mini, index


obj1 = Solu()
print(obj1.findmin([27, 31, 43, 45, 46, 5, 11, 13, 18, 19, 20]))
