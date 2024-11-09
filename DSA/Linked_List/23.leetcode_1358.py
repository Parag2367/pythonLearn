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


class Brute:
    """
    TC: O(n^2)
    SC: O(1)# as constant space we need a,b,c only
    """

    def countSub(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            char = set()
            for j in range(i, n):
                char.add(s[j])

                if len(char) == 3:
                    count += 1

        return count

    def brute_optimized(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            char = set()
            for j in range(i, n):
                char.add(s[j])

                if len(char) == 3:
                    count += (
                        n - j
                    )  # when we have reached 3 whatever will come will the substrings, so that is wht (n-j)
                    break

        return count


class optimal:
    """
    TC: O(n)
    SC: O(1)
    """

    def countSub(self, s: str) -> int:
        n = len(s)
        count = 0
        i = 0
        numbers = {"a": -1, "b": -1, "c": -1}

        while i < n:
            numbers[s[i]] = i

            if numbers["a"] >= 0 and numbers["b"] >= 0 and numbers["c"] >= 0:
                count += min(numbers.values()) + 1

            i += 1

        return count


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        temp = [-1] * 3
        cnt = 0
        for i in range(len(s)):
            temp[ord(s[i]) - ord("a")] = i
            if -1 not in temp:
                cnt += min(temp) + 1
        return cnt
