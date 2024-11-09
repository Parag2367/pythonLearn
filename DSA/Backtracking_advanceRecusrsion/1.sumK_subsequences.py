# class Solution:
#     def sumk(self, nums, k):
#         result = []

#         def backtrack(subset, index, total):
#             if total > k:
#                 return
#             if index >= len(nums):
#                 if total == k:
#                     result.append(subset.copy())
#                 return
#             subset.append(nums[index])
#             total = total + nums[index]
#             backtrack(subset, index + 1, total)
#             e = subset.pop()
#             total = total - e
#             backtrack(subset, index + 1, total)

#         a = backtrack([], 0, 0)
#         return a


# obj1 = Solution()
# print(obj1.sumk([1, 3, 0], 4))

# result = []


def backtrack(subset, index, total):
    if total > k:
        return
    if index >= len(nums):
        if total == k:
            result.append(subset.copy())
        return
    subset.append(nums[index])
    total = total + nums[index]
    backtrack(subset, index + 1, total)
    e = subset.pop()
    total = total - e
    backtrack(subset, index + 1, total)


result = []
nums = [1, 2, 3, 2, 2, 3, 4, 5]
k = 5
backtrack([], 0, 0)
print(result)


# def backtrack(subset, index, total):
#     if index >= len(nums):
#         if total == k:
#             result.append(subset.copy())
#             return True
#         return False
#     subset.append(nums[index])
#     total = total + nums[index]
#     if backtrack(subset, index + 1, total):
#         return True
#     e = subset.pop()
#     total = total - e
#     backtrack(subset, index + 1, total)


# nums = [1, 3, 0]
# k = 4
# print(backtrack([], 0, 0))
