"""
fruits and baskets
"""


class Solution:
    """
    brute:
    TC: O(n^2)
    SC: O(k) == O(1) as k is a constant value
    """

    def fruits(self, arr, k):  # k = no.of baskets
        max_length = 0
        n = len(arr)

        for i in range(n):
            fruits = set()
            for j in range(i, n):
                fruits.add(arr[j])
                if len(fruits) > k:
                    break

                max_length = max(max_length, j - i + 1)

        return max_length


obj1 = Solution()
print(obj1.fruits([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 3))


class Solu:
    """
    Better
    TC: O(2n)
    SC: O(k) == O(1)
    """

    def fruitsCollect(self, arr, k):
        max_length = 0
        left, right = 0, 0
        fruits = dict()
        n = len(arr)
        while right < n:
            fruits[arr[right]] = fruits.get(arr[right], 0) + 1

            while len(fruits) > k:  # to make count of types of fruits to k
                fruits[arr[left]] -= 1

                if (
                    fruits[arr[left]] == 0
                ):  # if it is not less than k and value has reduced to zero , so remove it
                    del fruits[arr[left]]

                left += 1

            max_length = max(max_length, right - left + 1)

            right = right + 1

        return max_length


obj2 = Solu()
print(obj2.fruitsCollect([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 2))


class Optimal:
    """
    TC: O(n)
    SC: O(1)
    """

    def collectFruits(self, arr: list, k: int) -> int:

        max_length, left, right = 0, 0, 0
        n = len(arr)
        fruits = dict()

        while right < n:
            fruits[arr[right]] = fruits.get(arr[right], 0) + 1

            if len(fruits) > k:
                fruits[arr[left]] -= 1

                if fruits[arr[left]] == 0:
                    del fruits[arr[left]]

                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


obj2 = Optimal()
print(obj2.collectFruits([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 2))
