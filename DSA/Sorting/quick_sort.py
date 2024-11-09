"""
qucik sort

TC: O(nlogn) for best and avg case, for worst case is O(n^2)
SC:

"""


def partition(arr, low, high):  # using this we will get partition index
    # picking a pivot we have four option for that fisrst_element,last_element,middle_element,random_element
    pivot = arr[low]
    # i will start from left, j from right, low is first element, high is last element
    i = low
    j = high

    # checking for left to right if it fails we have our i, check for first larger number then pivot
    while arr[i] <= pivot and i <= high - 1:
        i += 1
    # checking for right to left if it fails we have our j, check for first smaller number then pivot
    while arr[j] > pivot and j >= low + 1:
        j -= 1

    if i < j:
        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


# recursion will go on till low < high it will happen for each part
def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)  # this for choosing partiton element
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)


# arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]

arr = [34, 12, 35, 11, 36, 11, 37, 11, 38, 11]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
