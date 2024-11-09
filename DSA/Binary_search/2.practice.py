"""
You're given a sorted array 'a' of 'n' integers and an integer 'x'.

Find the floor and ceiling of 'x' in 'a[0..n-1]'.

Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.


Example:
Input: 
n=6, x=5, a=[3, 4, 7, 8, 8, 10]   

Output:
4

Explanation:
The floor and ceiling of 'x' = 5 are 4 and 7, respectively.
"""


def getFloorAndCeil(a, n, x):
    ceil = -1
    floor = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return x, x

        elif a[mid] > x:
            ceil = a[mid]
            high = mid - 1

        else:
            floor = a[mid]
            low = mid + 1

    return floor, ceil
