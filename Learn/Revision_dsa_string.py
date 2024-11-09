"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def len_longest(s: str):
    # TC: O(n^2)
    # SC: O(n) set
    n = len(s)
    maxi = 0

    for i in range(n):
        myset = set()

        for j in range(i, n):
            if s[j] in myset:
                break

            maxi = max(maxi, j - i + 1)

            myset.add(s[j])

    return maxi


def opt_longest(s: str):
    n = len(s)
    left = 0
    right = 0
    maxi = 0
    mydict = dict()

    while right < n:
        if s[right] in mydict:
            # isse yeh pta chala ki repeat kahanse shuru hua toh left wahan nhi hona chahiye
            left = max(left, mydict[s[right]] + 1)

        maxi = max(maxi, right - left + 1)
        mydict[s[right]] = right
        right += 1

    return maxi


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


def brackets(brac: str):
    n = len(brac)
    stack = []

    if n == 0:
        return

    if n == 1:
        return False

    if n % 2 == 1:
        return False

    for a in brac:
        if a == "(" or a == "{" or a == "[":
            stack.append(a)

        else:
            if len(stack) == 0:
                return False

            else:
                ch = stack.pop()

                if (
                    ch == "("
                    and a == ")"
                    or ch == "{"
                    and a == "}"
                    or ch == "["
                    and a == "]"
                ):

                    continue
                else:
                    return False

    return len(stack) == 0


"""
[3,6,8,12,15],7
"""


def insert(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
"""


def atleast(s):
    n = len(s)
    count = 0
    for i in range(n):
        myset = set()

        for j in range(i, n):
            myset.add(s[j])

            if len(myset) == 3:
                count += 1
    return count


def opt_atleast(s):
    n = len(s)
    hash_map = {"a": -1, "b": -1, "c": -1}
    count = 0

    for i in range(n):
        hash_map[s[i]] = i

        if hash_map["a"] == 0 and hash_map["b"] == 0 and hash_map["c"] == 0:
            count += min(hash_map.values()) + 1

    return count


"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


def max_ones_k(nums: list, k: int):
    n = len(nums)
    left, right = 0, 0
    maxi = 0
    zeroes = 0

    while right < n:
        if nums[right] == 0:
            zeroes += 1

        if zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        if zeroes <= k:
            maxi = max(maxi, right - left + 1)
        zeroes += 1

    return maxi


"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 
Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
"""


def max_card_points(cards, k):
    n = len(cards)

    if k == n:
        return sum(cards)

    left_sum = 0
    right_sum = 0
    maxi = 0

    for i in range(k):
        left_sum += cards[i]

    maxi = left_sum

    right_index = n - 1
    for i in range(k - 1, -1, -1):
        left_sum -= cards[i]
        right_sum += cards[right_index]
        right_index -= 1

        maxi = max(maxi, (left_sum + right_sum))

    return maxi


"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []

        for i, row in enumerate(board):
            for j, d in enumerate(row):
                if d != ".":
                    seen.extend(
                        [(d, i), (j, d), (d, i // 3, j // 3)]
                    )  # these tuples never interfere!

        return len(set(seen)) == len(seen)
