"""
Problem statement
You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 'm(1/n)'. If the 'nth root is not an integer, return -1.



Note:
'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


Example:
Input: ‘n’ = 3, ‘m’ = 27

Output: 3

Explanation: 
3rd Root of 27 is 3, as (3)^3 equals 27.
"""


class Optimal:
    def mroot(self, m, n):
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if mid**m == n:
                return mid

            elif mid**m > n:
                high = mid - 1

            else:
                low = mid + 1

        return -1


obj1 = Optimal()
print(obj1.mroot(3, 125))
