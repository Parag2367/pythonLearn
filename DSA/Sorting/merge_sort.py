"""
Merge sort:

TC : O(nlogn) : for all cases , 
SC : O(n) because we are using merged = []  it will take n space
"""


def merge_sort(arr):
    # condition to stop recursion
    if len(arr) <= 1:
        return arr

    # dividing array in two part
    mid = len(arr) // 2

    # two prts of array
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursion on left and right parts
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # calling for merge when the recursion is stopped
    return merge(left_half, right_half)


# merge function to merge the array in sorted way, or sort is happened using this function
def merge(left, right):
    merged = []
    i, j = 0, 0

    # condition to check when niether i or j is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1
    # these below condition will only work once above while is false , which means eith i >= len(left) or j >= len(right)

    # condition to append the array if j is exhausted or j is out of index
    # happens when len(right) is smaller then len(left)
    while i < len(left):
        merged.append(left[i])
        i = i + 1

    # condition to check if i is exhausted or i is out of index
    # happens when len(right) is greater is len(left)
    while j < len(right):
        merged.append(right[j])
        j = j + 1

    return merged


print(merge_sort([2, 2, 0, 0, 1, 1]))
