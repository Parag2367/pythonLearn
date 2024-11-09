"""
You are given an array 'arr' of length 'n' containing integers within the range '1' to 'x'.
Your task is to count the frequency of all elements from 1 to n.

Note:
You do not need to print anything. Return a frequency array as an array in the function such that index 0 represents the frequency of 1, 
index 1 represents the frequency of 2, and so on.

Input: "n" = 6 "x" = 9 "arr" = [1, 3, 1, 9, 2, 7]    
Output: [2, 1, 1, 0, 0, 0]
"""

from typing import List


def countFreq(n: int, x: int, arr: List[int]):
    hash_list = [
        0
    ] * n  # usually it is m but in this case we only want to show n numbers list

    for a in arr:
        if (
            a > n
        ):  # if number in list is greater then n , we don't want to have them in our final list
            continue

        hash_list[a - 1] += 1  # index of zero should represent freq of 1,and so on
    return hash_list


print(countFreq(6, 9, [1, 3, 1, 9, 2, 7]))
