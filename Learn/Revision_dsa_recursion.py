"""
BASE APPROACH: picking and unpicking
"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
"""


def generate_parenthesis_valid(n: int):
    def backtrack(left, right, s):
        if len(s) == 2 * n:
            result.append(s)
            return

        if left < n:
            backtrack(left + 1, right, s + "(")

        if right < left:
            backtrack(left, right + 1, s + ")")

    result = []
    backtrack(0, 0, "")
    return result


print(generate_parenthesis_valid(3))


def generate_parenthesis(n: int):
    def backtrack(left, right, s):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(left + 1, right, s + "(")

        if right < n:
            backtrack(left, right + 1, s + ")")

    result = []
    backtrack(0, 0, "")
    return result


print(generate_parenthesis(2))


"""
All possible Subsequences 

"""


def subsequences(nums: list, n: int):
    def subsets(arr: list, index: int):
        if index >= n:
            result.append(arr.copy())
            return

        arr.append(nums[index])
        subsets(arr, index + 1)
        arr.pop()
        subsets(arr, index + 1)

    result = []
    subsets([], 0)
    return result


print(subsequences([1, 2, 3], 3))


def str_subsequnces(mystr: str, n: int):
    def backtrack(arr, index):
        if index >= n:
            result.append(arr[:])
            return

        backtrack(arr + mystr[index], index + 1)
        backtrack(arr, index + 1)

    result = []
    backtrack("", 0)
    return result


print(str_subsequnces("abc", 3))


"""
Subsequence whose sum is equals to k
"""


def subsum(nums: list, k: int, n):
    def subset(arr: list, index, total):
        if total > k:
            return

        if index >= n:
            if total == k:
                result.append(arr.copy())
            return

        arr.append(nums[index])
        total = total + nums[index]
        subset(arr, index + 1, total)

        e = arr.pop()
        total = total - e
        subset(arr, index + 1, total)

    result = []
    subset([], 0, 0)
    return result


print(subsum([1, 2, 3, 7, 1, 3, 4], 5, 7))


"""
Find one subsequences with sum=K
"""


def one_sub(nums: list, k: int):
    def backtrack(arr: list, index, total):
        if total > k:
            return

        if index >= len(nums):
            if total == k:
                result.append(arr.copy())
                return True
            return False

        arr.append(nums[index])
        total = total + nums[index]
        if backtrack(arr, index + 1, total):
            return True
        e = arr.pop()
        total = total - e
        return backtrack(arr, index + 1, total)

    result = []
    backtrack([], 0, 0)

    return result


print(one_sub([1, 2, 3, 7, 1, 3, 4], 5))


"""
count of subsequences with sum == k
"""


def count_sub(nums: list, k: int):
    def backtrack(arr: list, index: int, total: int):
        if total > k:
            return

        if index > len(nums):
            if total == k:
                return 1
            return 0

        arr.append(nums[index])
        total = total + nums[index]
        left = backtrack(arr, index + 1, total)

        e = arr.pop()
        total = total - e
        right = backtrack(arr, index + 1, total)

        return left + right

    count = backtrack([], 0, 0)
    print(count)


"""
Combination sum , you can use any number any number of times
"""


def comb_sum(nums: list, target):
    def backtrack(arr, index, target):
        if target == 0:
            result.append(arr.copy())
            return
        if index >= len(nums):
            return

        if nums[index] <= target:
            arr.append(nums[index])
            target -= nums[index]
            backtrack(arr, index, target)
            e = arr.pop()
            target += e

        backtrack(arr, index + 1, target)

    result = []
    backtrack([], 0, target)
    return result


print(comb_sum([2, 3, 6, 7], 7))


"""
40. Combination Sum II, it should not have same combination
"""


def comb_sum2(nums: list, target: int):  # the list should be sorted for this
    # nums.sort()

    def backtrack(arr, index, target):
        if target == 0:
            result.append(arr.copy())
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            arr.append(nums[i])
            # target -= nums[i]
            backtrack(arr, i + 1, target - nums[i])
            arr.pop()

    result = []
    backtrack([], 0, target)

    return result


print(comb_sum2([1, 1, 1, 2, 2], 4))
print(comb_sum2([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))


"""
Combination Sum III, it should not have same combination and of a given length
"""


def comb_sum3(mylist: list, k, target):
    def backtrack(arr: list, index, target):
        if target == 0 and len(arr) == k:
            result.append(arr.copy())
            return

        for i in range(index, len(mylist)):
            if i > index and mylist[i] == mylist[i - 1]:
                continue

            if mylist[i] > target:
                break

            arr.append(mylist[i])
            backtrack(arr, i + 1, target - mylist[i])
            arr.pop()

    result = []
    backtrack([], 0, target)

    return result


"""
Subset sum
"""

# Bruteforce


def subset_sum(nums: list):
    def backtrack(arr, index):
        if index >= len(nums):
            result.append(sum(arr.copy()))
            return

        arr.append(nums[index])
        backtrack(arr, index + 1)
        arr.pop()
        backtrack(arr, index + 1)

    result = []
    backtrack([], 0)

    result.sort()
    return result


print(subset_sum([3, 1, 2]))

# Optimal


def subset_sum_optimal(nums: list):
    def backtrack(total, index):
        if index >= len(nums):
            result.append(total)
            return

        backtrack(total + nums[index], index + 1)
        backtrack(total, index + 1)

    result = []
    backtrack(0, 0)

    result.sort()
    return result


print(subset_sum_optimal([3, 1, 2]))


"""
Subset sum 2
"""


def subset_sum2(nums: list):
    def backtrack(arr, index):
        nums.sort()

        result.append(arr.copy())
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            arr.append(nums[i])
            backtrack(arr, i + 1)
            arr.pop()

    result = []
    backtrack([], 0)

    return result


print(subset_sum2([4, 4, 4, 1, 4]))


"""
Palidrome Partitioning
"""


def palindrome_partition(mystr: str):

    def isPalindrome(s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def backtrack(substring, index):
        if index >= len(mystr):
            result.append(substring[:])

        for i in range(index, len(mystr)):
            if isPalindrome(mystr, index, i):
                substring.append(mystr[index : i + 1])
                backtrack(substring, i + 1)
                substring.pop()

    result = []
    backtrack([], 0)

    return result


print(palindrome_partition("aabb"))
