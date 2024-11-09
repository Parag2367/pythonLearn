"""
character hashing (not efficent , just understanding the concept)
"""

# string = "aeroplane"
# char_hash = [0] * 26

# for ch in string:
#     char_hash[ord(ch) - ord("a")] += 1

# print(char_hash)


# chr = input("Enter character to check its count = ")
# print(char_hash[ord(chr) - ord("a")])


"""
Efficient way is dictionary that we have already used : because it is not taking extra memory though both have same TC
"""

string = "aerooplaaane"

hash_map = {}

for ch in string:
    # hash_map[ch] = (
    #     hash_map[ch] + 1
    # )  # this will give key error as dictionary is empty , so we have to iitiate it first, see below line

    hash_map[ch] = hash_map.get(ch, 0) + 1

print(hash_map)
chr = input("enter character whose count you want = ")
print(f"count is {hash_map[chr]}")
