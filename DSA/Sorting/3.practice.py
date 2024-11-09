"""
Check if the given array is sorted or not

"""


class Solu:
    def checkSort(self, arr: list):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return 0
        return 1


arr = [1, 2, 3, 4]
arr1 = [2, 3, 1, 0]

obj1 = Solu()
print(obj1.checkSort(arr1))
