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


class Brute:
    """
    TC: O(n^2)
    SC: O(n)
    """

    def lonSub(self, s: str):
        if len(s) == 0:
            return 0
        n = len(s)
        maxi = 0
        for i in range(n):
            myset = set()  # doing this to reset every time i moves to next position

            for j in range(i, n):
                if s[j] in myset:  # if same character found break
                    break
                maxi = max(maxi, j - i + 1)  # length = j-i+1
                myset.add(s[j])

        return maxi


class Solution:
    """
    TC: O(n)
    SC: O(n)
    """

    def longsubstring(self, s: str) -> int:
        n = len(s)
        max_count = 0
        hash_map = dict()
        left = 0
        right = 0

        while right < n:
            if s[right] in hash_map:
                left = max(hash_map[s[right]] + 1, left)
            hash_map[s[right]] = right  # continously happening
            max_count = max(max_count, (right - left + 1))  # continously happening
            right = right + 1

        return max_count


obj1 = Solution()
print(obj1.longsubstring("abba"))


class Solu:
    def lenSub(self, s: str):
        n = len(s)
        mydict = dict()
        max_length, left, right = 0, 0, 0

        while right < n:
            if s[right] in mydict:  # condition when we find same character
                left = max(
                    mydict[s[right]] + 1, left
                )  # used max because for use cases like 'abba','abca' etc
            mydict[s[right]] = right
            max_length = max(max_length, right - left + 1)

            right += 1
        return max_length
