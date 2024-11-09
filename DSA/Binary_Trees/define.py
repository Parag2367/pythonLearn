class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
        Drinks
    Hot        Cold
"""

drinks = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")

drinks.left = hot
drinks.right = cold


print(drinks)
print(drinks.data)

print(drinks.left)
print(hot)
print(drinks.left.data)
