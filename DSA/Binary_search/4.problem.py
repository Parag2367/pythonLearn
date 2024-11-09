"""
Problem statement
You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.



Find the total number of occurrences of 'x' in the array/list.



Example:
Input: 'n' = 7, 'x' = 3
'arr' = [1, 1, 1, 2, 2, 3, 3]

Output: 2

Explanation: Total occurrences of '3' in the array 'arr' is 2.
"""


def count(arr, n: int, x: int) -> int:
    def binary(arr, x, search_left):
        ind = -1
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                ind = mid
                if search_left:
                    high = mid - 1
                else:
                    low = mid + 1

            elif arr[mid] > x:
                high = mid - 1

            else:
                low = mid + 1

        return ind

    left = binary(arr, x, True)
    if left == -1:
        return 0
    right = binary(arr, x, False)

    return right - left + 1


print(count([2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19], 15, 10))


### Another approach
"""
using lower bound and upper bound, as array is sorted so we can apply easily
as lower bound >=num, and upper bound gives only greater
"""


class solunew:
    def optimal2(self, nums, target):
        def lower(nums, target):
            n = len(nums)
            ans = n
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1

                else:
                    low = mid + 1

            return ans

        def upper(nums, target):
            n = len(nums)
            ans = n
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    ans = mid
                    high = mid - 1

                else:
                    low = mid + 1

            return ans

        low = lower(nums, target)
        high = upper(nums, target)

        return high - low


obj2 = solunew()
print(obj2.optimal2([2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19], 10))
