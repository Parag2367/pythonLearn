"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

import math


class Brute:
    def total_hours(self, piles, k):
        total = 0

        for i in range(len(piles)):
            total += math.ceil(piles[i] / k)

        return total


class rate(Brute):
    def rate(self, piles, hour):
        m = max(piles)
        low = 1
        high = m
        ans = 1
        for i in range(1, m + 1):
            total = self.total_hours(piles, i)
            if total <= hour:
                return i


obj1 = rate()
print(obj1.rate([3, 6, 7, 11], 8))


# optimal way
class Optimal:
    def total_hours(self, piles, k):
        total = 0

        for i in range(len(piles)):
            total += math.ceil(piles[i] / k)

        return total


class krate(Optimal):
    def rate(self, piles, hour):
        m = max(piles)
        low = 1
        high = m
        ans = 1

        while low <= high:
            mid = (low + high) // 2
            total = self.total_hours(piles, mid)
            if total <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


obj2 = krate()
print(obj2.rate([3, 6, 7, 11], 8))


from typing import List


# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int):
#         def total_hours(piles, k):
#             total = 0

#             for i in range(len(piles)):
#                 total = total + math.ceil(piles[i] / k)

#             return total

#         m = max(piles)
#         low = 1
#         high = m
#         ans = 1

#         while low <= high:
#             mid = (low + high) // 2
#             total = total_hours(piles, mid)

#             if total <= h:
#                 ans = mid
#                 high = mid - 1

#             else:
#                 low = mid + 1

#         return ans


# another way
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int):
        low = 1
        high = max(piles)
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            total = 0

            for pile in piles:
                total += math.ceil(pile / mid)

            if total > h:
                low = mid + 1

            else:
                ans = mid
                high = mid - 1

        return ans
