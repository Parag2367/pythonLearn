import copy

a = [[41, 12, 83], [44, 35, 16], [767, 38, 19]]

b = copy.deepcopy(a)

print(a, id(a))
print(b, id(b))
print("--------")
a[0][0] = 100
print(a)
print(b)
