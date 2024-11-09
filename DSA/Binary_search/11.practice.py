"""
Problem statement
You are given a positive integer ‘n’.



Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).



Example:
Input: ‘n’ = 7

Output: 2

Explanation:
The square root of the number 7 lies between 2 and 3, so the floor value is 2.
"""

import math

a = int(math.sqrt(9))
print(a)


# another:
def root(n):
    ans = 1

    for i in range(n):
        if i * i <= n:
            ans = i
        else:
            break

    return ans


###
class Optimal:
    def root(self, n):
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= n:
                low = mid + 1

            else:
                high = mid - 1
        return high
