"""
Write a function to check if a given string is a palindrome. Use 2
methods. One is using slicing and other using loops. Both should be
written. So basically make 2 functions for each.

"""

# def isPalindrome(mystr: str) -> bool:
#     newstr = ""
#     for a in mystr[::-1].lower():
#         newstr += a

#     return mystr == newstr


# def isPalin(mystr: str) -> bool:
#     return mystr.lower() == mystr[::-1].lower()


# print(isPalindrome("paragarap"))
# print(isPalindrome("paragarapa"))

##optimized way

# def isPalindrome(mystr: str) -> bool:
#     n = len(mystr)
#     for i in range(n // 2):
#         if mystr[i] != mystr[n - i - 1]:
#             return False

#     return True


# print(isPalindrome("paragarap"))
# print(isPalindrome("paragarapa"))

"""
Write a program to generate a list of even numbers between 1 and 20
using list comprehension.

"""

# new = [a for a in range(1, 11) if a % 2 == 0]
# print(new)


"""
Write a function that takes a string as input and returns only vowels in
that string.
"""


# def onlyVowel(mystr: str) -> str:
#     vowels = ["a", "e", "i", "o", "u"]
#     new_str = ""
#     for ch in mystr:
#         if ch in vowels:
#             new_str += ch
#         else:
#             continue

#     return new_str


# print(onlyVowel("parag is a nice human being"))


"""
Write a function to find the contiguous subarray with the largest sum
in a given list of integers.
"""


# def largestSum(mylist: list) -> float:
#     largest = 0
#     for a in mylist:
#         total = 0
#         for i in a:
#             total = total + i
#         if total > largest:
#             largest = total

#     return largest


# mylist = [[1, 2, 3], [2, -3, -4], [3, 3, 3, 4, 5], [10, 1]]
# print(largestSum(mylist))


"""
. Python program to find second largest number in a list. If 2nd largest
element does not exists. Return -1.

"""


# def secondLargest(mylist: list) -> float:
#     largest = float("-inf")
#     second_largest = float("-inf")

#     for a in mylist:
#         if a > largest:
#             second_largest = largest
#             largest = a
#         elif a > second_largest and a != largest:
#             second_largest = a

#     if second_largest == float("-inf"):
#         return -1

#     else:
#         return second_largest


# print(secondLargest([2, 2, 2, 2, 2, -2]))


"""
Write a program for Sum of number digits in List.
"""


# def sumOfDigits(mylist: list):
#     new_list = []
#     for a in mylist:
#         total = 0
#         while a > 0:
#             total += a % 10
#             a = a // 10
#         new_list.append(total)
#     print(new_list)


# sumOfDigits([12, 23, 34, 44])


"""
Write a program to find Maximum frequency character in String.
Return/Print the character which comes the most times in that string.

"""


# def maxfreq(mystr: str):
#     new_str = {}
#     for a in mystr:
#         if a in new_str:
#             new_str[a] = new_str[a] + 1
#         else:
#             new_str[a] = 1

#     result = sorted(new_str.items(), key=lambda x: x[1], reverse=True)
#     print(result[0])


# maxfreq("my name isparag")


#########################
# def maxfreq(mystr: str):
#     new_dict = {}
#     for ch in mystr:
#         new_dict[ch] = new_dict.get(ch, 0) + 1

#     max_freq = 0
#     max_freq_chr = ""

#     for key, value in new_dict.items():
#         if value > max_freq:
#             max_freq = value
#             max_freq_chr = key

#     return max_freq_chr


# print(maxfreq("my name isparag"))


"""
Given a string of size n, write functions to perform following operations
on string:
Left (Or anticlockwise) rotate the given string by d elements (where d
<= n).
Right (Or clockwise) rotate the given string by d elements (where d <=
n).
"""

"""
"pythonprogramming"
d = 5

clock = onprogrammingpyth
anti = mingpythonprogram

"""


# def rotateClock(mystr: str, d: int) -> str:
#     n = len(mystr)
#     d = d % n
#     newstr = mystr[d:] + mystr[:d]
#     return newstr


# def rotateAnti(mystr: str, d: int) -> str:
#     n = len(mystr)
#     d = d % n
#     newstr = mystr[(n - d) :] + mystr[: (n - d)]
#     return newstr


# print(rotateClock("pythonprogramming", 4))
# print(rotateAnti("pythonprogramming", 4))

"""
# # Ways to sort list of dictionaries by values in Python – Using lambda function.

# """
# list_of_dicts = [
#     {"name": "Anirudh", "age": 25},
#     {"name": "Nihar", "age": 20},
#     {"name": "Prem", "age": 30},
# ]
# final = sorted(list_of_dicts, key=lambda x: x["age"])
# print(final)


"""
Remove all duplicates words from a given sentence.

"""


# def removeDup(mystr: str) -> str:
#     new_str = []
#     for a in mystr.split():
#         if a not in new_str:
#             new_str.append(a)
#         else:
#             continue

#     final = " ".join(new_str)
#     return final


# print(removeDup("python is great and java is also great"))

# # another approach
# # in this order does not matter


# def remove(mystr: str) -> str:
#     new_str = set(mystr.split())
#     final = " ".join(new_str)
#     return final


# print(remove("python is great and java is also great"))


"""
Python Program for Find sum of odd factors of a number
"""


# def sumOddFact(num: int) -> int:
#     x = num
#     factor = []
#     for a in range(1, num + 1, 2):
#         if x % a == 0:
#             factor.append(a)

#         else:
#             continue
#     return sum(factor)


# print(sumOddFact(30))
# print(sumOddFact(33))


"""
Write a python program for a given long integer, we need to find if the
difference between sum of odd digits and sum of even digits is 0 or not.
The indexes start from zero (0 index is for the leftmost digit).
"""


# def sumOE(num: float) -> bool:
#     x = num
#     number = str(x)
#     even = [int(number[a]) for a in range(0, len(number)) if a % 2 == 0]
#     odd = [int(number[a]) for a in range(0, len(number)) if a % 2 != 0]

#     return sum(odd) == sum(even)


# print(sumOE(1212112))


def isDiff0(n):
    first = 0
    second = 0
    flag = True
    while n > 0:
        digit = n % 10
        if flag:
            first += digit
        else:
            second += digit
        if flag:
            flag = False
        else:
            flag = True
        n = int(n / 10)
    if first - second == 0:
        return True
    return False


n = 1243
if isDiff0(n):
    print("Yes")
else:
    print("No")

"""
# Write a program to get/print the number of
# characters, words, spaces and lines in a file.
"""


# def count(filename: str) -> dict:
#     char_count = word_count = space_count = line_count = 0

#     with open(filename, "r") as file:
#         for line in file:
#             line_count += 1
#             char_count += len(line)
#             word_count += len(line.split())
#             space_count += line.count(" ")

#     return {
#         "characters": char_count,
#         "words": word_count,
#         "spaces": space_count,
#         "lines": line_count,
#     }


# filename = "hello.txt"
# all_count = count(filename)

# # Print the results
# print(f"Number of characters = {all_count['characters']}")
# print(f"Number of words = {all_count['words']}")
# print(f"Number of spaces = {all_count['spaces']}")
# print(f"Number of lines = {all_count['lines']}")
