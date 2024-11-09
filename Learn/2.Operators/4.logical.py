"""
  AND ,OR, NOT (to compare two or more result)
  Answer is always in bool
"""

phy = 67
chem = 99

print(phy > 33 and chem > 33)
print(phy > 70 or chem > 33)

print(not phy > 33)

a = True
b = False

print(not a or b)

print(not phy > 70 or not chem > 33)
# not F or not T
# T or F
# True
