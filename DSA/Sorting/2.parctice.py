"""
You have been given an array ‘a’ of ‘n’ unique non-negative integers.
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2.

Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
"""

# better:


def second(arr: list):
    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")

    for a in arr:
        smallest = min(smallest, a)
        largest = max(largest, a)

    for i in range(0, len(arr)):
        if arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]

        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]


# optimal


def second_second(num: int, arr: list):
    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")

    for a in arr:
        if a > largest:
            second_largest = largest
            largest = a

        elif a > second_largest and a != largest:
            second_largest = a

        if a < smallest:
            second_smallest = smallest
            smallest = a

        elif a < second_smallest and a != smallest:
            second_smallest = a

    return second_largest, second_smallest


print(second_second(6, [2, 3, 4, 5, 4, 3, 7]))
