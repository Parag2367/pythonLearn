"""
You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’, and your task is to find whether ‘num’ is present in the array or not.

If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. Else, return -1.

Example:
Input: ‘n’ = 5, ‘num’ = 4 
'arr' =  [6,7,8,4,1] 

Output: 3

Explanation:
4 is present at the 3rd index.

"""


# anyway it always gives first position
class Solu:
    """
    TC: O(n)
    """

    def search(self, n: int, num: int, arr: list) -> int:
        for i in range(0, n):
            if arr[i] == num:
                return i
        return -1


obj1 = Solu()
print(obj1.search(7, 4, [6, 7, 8, 0, 0, 5, 1]))
