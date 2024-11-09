"""
Given an array 'v' of 'n' numbers.

Your task is to find and return the highest and lowest frequency elements.
If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.

Example:
Input: "n" = 6, 'v' = [1, 2, 3, 1, 1, 4]

Output: 1 2

Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].
"""

from typing import List


# def max_min(n: int, arr: List[int]):
#     hash_map = {}
#     for a in arr:
#         hash_map[a] = hash_map.get(a, 0) + 1

#     max = float("-inf")
#     keymax = float("inf")
#     min = float("inf")
#     keymin = float("inf")

#     for k, v in hash_map.items():
#         if (
#             v > max or v == max and k < keymax
#         ):  # this 'and' condition is for returning smallest element who have same frequency
#             max = v
#             keymax = k
#         if (
#             v < min or v == min and k < keymin
#         ):  # this 'and' condition is for returning smallest element who have same frequency
#             min = v
#             keymin = k

#     return [keymax, keymin]


# print(max_min(6, [1, 2, 3, 1, 1, 4]))

"""
self practice
"""


def max_min(num: int, arr: List[int]):
    hash_map = {}
    for a in arr:
        hash_map[a] = hash_map.get(a, 0) + 1
    # same logic that we use to find max value, here we have to find max key and max value
    max = float("-inf")
    maxkey = float("inf")
    min = float("inf")
    minkey = float("inf")

    for key, value in hash_map.items():
        if value > max or value == max and key < maxkey:
            max = value
            maxkey = key
        if value < min or value == min and key < minkey:
            min = value
            minkey = key

    return [maxkey, minkey]


print(max_min(6, [1, 2, 3, 5, 1, 1]))
