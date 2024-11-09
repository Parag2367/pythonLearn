"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solu:
    """
    TC: O(n^2)
    Sc: O(n)
    """

    def besttime(self, nums: list):
        n = len(nums)
        max_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                profit = nums[j] - nums[i]
                if profit > max_profit:
                    max_profit = profit

        print(max_profit)


obj1 = Solu()
obj1.besttime([7, 1, 5, 3, 6, 4])


# Optimal solution best way
class Optimal:
    """
    Dynamic programming
    TC: O(n)
    Sc: O(1)
    """

    def best(self, nums):
        max_profit = 0
        min_price = float("inf")

        for i in range(len(nums)):
            min_price = min(min_price, nums[i])
            max_profit = max(max_profit, (nums[i] - min_price))

        return max_profit


obj1 = Optimal()
print(obj1.best([7, 1, 5, 3, 6, 4]))


# another way
class Optimal_1:
    """
    Sliding window
    TC: O(n)
    SC: O(1)
    """

    def besttime(self, nums):
        l = 0
        max_profit = 0
        for i in range(1, len(nums)):
            profit = nums[i] - nums[l]
            if profit > 0:
                max_profit = max(profit, max_profit)

            else:
                l = i

        print(max_profit)


obj1 = Optimal_1()
obj1.besttime([7, 6, 5, 4, 3])


# def test(nums):
#     max_profit = 0
#     n = len(nums)
#     l = 0

#     for i in range(1, n):
#         profit = nums[i] - nums[l]

#         if profit > 0:
#             max_profit = max(max_profit, profit)

#         else:
#             l = i
