"""
hashing
"""

# lst = []
# list_length = int(input("enter length of list "))
# # the list
# for a in range(1, list_length + 1):
#     num = int(input("enter number "))
#     lst.append(num)
# print(lst)

# # pre compute , Hashing procedure starts here

# hash_list = [0] * 15  # 15 is the max number in list

# for num in lst:
#     hash_list[num] += 1

# print(hash_list)


# number = int(input("Enter number to count = "))
# print(f"{number} has occured {hash_list[number]} times")  # fetch


"""
most efficient way is dictionary : because it is not taking extra memory ,
will work only for 0 and positive integers of list ,
as we create a hash_list of 0 with index as the values to check though both have same TC
"""

lst = []
list_length = int(input("enter length of list "))
# the list
for a in range(1, list_length + 1):
    num = int(input("enter number "))
    lst.append(num)
print(lst)


hash_map = {}
for num in lst:
    hash_map[num] = hash_map.get(num, 0) + 1

print(hash_map)
number = int(input("Enter number to count = "))
print(f"count is {hash_map[number]}")
