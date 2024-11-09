"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""


class Solution:
    """
    Brute:
    TC : O(n^2)
    SC : O(n)
    """

    def repeat(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0
        max_freq = 0
        for i in range(n):
            hash_map = dict()

            for j in range(i, n):
                hash_map[s[j]] = hash_map.get(s[j], 0) + 1
                max_freq = max(max_freq, hash_map[s[j]])
                changes = (j - i + 1) - max_freq

                if changes > k:
                    break
                max_length = max(max_length, j - i + 1)
        return max_length


obj1 = Solution()
print(obj1.repeat("ABBA", 2))
