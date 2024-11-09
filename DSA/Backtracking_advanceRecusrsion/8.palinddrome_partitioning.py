"""
Palindrome partitioning
"""


def palindrome_part(mystr: str):
    def is_palindrome(s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def backtrack(substring, index):
        if index >= len(mystr):
            result.append(substring[:])
            return

        for i in range(index, len(mystr)):
            if is_palindrome(mystr, index, i):
                substring.append(mystr[index : i + 1])
                backtrack(substring, i + 1)
                substring.pop()

    result = []
    backtrack([], 0)

    return result


print(palindrome_part("aabb"))
