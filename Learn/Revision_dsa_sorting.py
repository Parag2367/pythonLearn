"""
You have been given an array ‘a’ of ‘n’ unique non-negative integers.
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2.

Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
"""


def ss(nums: list):
    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("-inf")

    for a in nums:
        if a > largest:
            second_largest = largest
            largest = a

        elif a > second_largest and a != largest:
            second_largest = a

        if a < smallest:
            second_smallest = smallest
            smallest = a

        elif a < second_smallest and a != smallest:
            smallest = a

    return second_smallest, second_largest


"""
Check if array is sorted and rotated
Time complexity = O(N) where N is the number of elements in list
Because we looping through the array only once

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
Space complexity = O(1)

"""


def check(nums: list):
    n = len(nums)
    rotation = 0

    for i in range(0, n):
        if (
            nums[i] > nums[(i + 1) % n]
        ):  # doing this if it is more then 1 then not proper
            rotation += 1
        if rotation > 1:
            return False

    return True  # this is for if nums[i] < nums[(i+1)%n]


"""
Remove Duplicates
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


def dup_r(nums: list) -> int:
    mydict = dict()

    for a in nums:
        mydict[a] = 0

    j = 0
    for a in mydict:
        nums[j] = a
        j += 1

    return j + 1


def dup_op(nums: list) -> int:  # two pointer approch
    n = len(nums)
    i = 0

    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    return i + 1


"""
Given an array 'arr' containing 'n' elements, rotate this array left once and return it.
Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.
Example:
Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation: We moved the 2nd element to the 1st position, and 3rd element to the 2nd position, and 4th element to the 3rd position, and the 5th element to the 4th position, and move the 1st element to the 5th position.
"""

"""
TC: O(n) as it is using for loop which is checking every element in that array
SC: O(1)
"""


def rev_arr(nums: list):
    n = len(nums)
    temp = nums[0]
    for i in range(0, n - 1):
        nums[i] = nums[i + 1]
    nums[-1] = temp
    return nums


"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


class Solution:
    def moveZeroes(self, nums: list):
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == 0:
                break
            i += 1
        else:
            return

        j = i + 1
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

            j += 1

        return nums


"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""


def cons_ones(nums: list):
    count = 0
    maxi = 0

    for a in nums:
        if a == 1:
            count += 1
        else:
            maxi = max(count, maxi)
            count = 0

    print(max(count, maxi))  # why used max here because for last iteration


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def two_sum(nums: list, target: int):
    hash_map = dict()
    n = len(nums)
    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hash_map.items():
            return [i, hash_map[remaining]]

        hash_map[nums[i]] = i


"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

constraint = nums is either in 0,1,2
"""


def colors(nums: list):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for a in nums:
        if a == 0:
            cnt0 += 1
        if a == 1:
            cnt1 += 1
        if a == 2:
            cnt2 += 1

    nums[:] = [0] * cnt0 + [1] * cnt1 + [2] * cnt2

    return nums


def sort_colors(nums: list):
    # using Dutch National Flag algorithm , three pointer
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


"""
Majority element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
"""
# majority element is an element which comes more then n/2 times
# moore's voting algo


def majority(nums: list):
    n = len(nums)
    count = 0
    candidate = nums[0]

    for i in range(n):
        if nums[i] == candidate:
            count += 1

        else:
            count -= 1

        if count == 0:
            candidate = nums[i]
            count = 1

    a = candidate
    count = 0
    for i in range(n):
        if nums[i] == a:
            count += 1

    if count > len(nums) // 2:
        return a
    else:
        return -1


"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
"""
# kadanes algorithm


def max_sum(nums: list):
    maxi = float("-inf")
    sum = 0
    n = len(nums)

    for i in range(n):
        sum = sum + nums[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi


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


# dynamic programming
def besttime(nums: list):
    min_price = float("inf")
    profit = 0
    n = len(nums)
    for i in range(n):
        min_price = min(nums[i], min_price)
        profit = max(profit, (nums[i] - min_price))

    return profit


# sliding window:
def best(nums: list):
    l = 0
    max_profit = 0

    for i in range(len(nums)):
        profit = nums[i] - nums[l]
        if profit > 0:
            max_profit = max(profit, max_profit)

        else:
            l = i


"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
"""


def alter(nums: list):
    n = len(nums)
    i, j = 0, 1
    res = [0] * n
    for k in range(n):
        if nums[i] > 0:
            res[i] = nums[k]
            i += 2

        else:
            res[i] = nums[k]
            j += 2

    return res


"""
Problem statement
There is an integer array ‘a’ of size ‘n’.

An element is called a Superior Element if it is greater than all the elements present to its right.
You must return an array all Superior Elements in the array ‘a’.

Note:

The last element of the array is always a Superior Element. 
Example

Input: a = [1, 2, 3, 2], n = 4

Output: 2 3

Explanation: 
a[ 2 ] = 3 is greater than a[ 3 ]. Hence it is a Superior Element. 
a[ 3 ] = 2 is the last element. Hence it is a Superior Element.
The final answer is in sorted order.
"""


def superior(nums: list):
    n = len(nums)
    maxi = float("-inf")
    result = []

    for i in range(n - 1, -1, -1):
        if nums[i] > maxi:
            result.append(nums[i])
            maxi = nums[i]

    return result


"""
There is an integer array ‘A’ of size ‘N’.

A sequence is successive when the adjacent elements of the sequence have a difference of 1.

You must return the length of the longest successive sequence.

Note:

You can reorder the array to form a sequence. 
For example,

Input:
A = [5, 8, 3, 2, 1, 4], N = 6
Output:
5
Explanation: 
The resultant sequence can be 1, 2, 3, 4, 5.    
The length of the sequence is 5.
"""


def succesive(nums: list):
    myset = set()
    for a in nums:
        myset.add(a)

    longest = 0
    for a in myset:
        if a - 1 not in myset:
            x = a
            count = 1

            while x + 1 in myset:
                count += 1
                x += 1

            longest = max(longest, count)

    return longest


def success(nums: list):
    myset = set()
    count = 0

    for a in nums:
        myset.add(a)

    long = 0

    for a in myset:
        if a - 1 not in myset:
            count = 1
            x = a

            while x + 1 in myset:
                count += 1
                x += 1

            long = max(long, count)

    return long


"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 
"""


def count_sum(nums: list, k: int):
    d = {0: 1}
    sums = 0
    count = 0

    for i in range(len(nums)):
        sums += nums[i]

        if sums - k in d:  # this is imp sums-k if it is available
            count += d[sums - k]

        if sums in d:
            d[sums] += 1

        else:
            d[sums] = 1

    return count


"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""


def triple_sum(nums: list):
    n = len(nums)
    result = []
    i = 0
    a = nums[i]
    target = -a
    hash_map = dict()
    for j in range(n):
        rem = target - nums[j]

        if rem in hash_map:
            if len(result) == 0 or result[-1] != [a, rem, nums[j]]:
                result.append([a, rem, nums[j]])

            else:
                i += 1

        else:
            hash_map[nums[j]] = j

    return result
