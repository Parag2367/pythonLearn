# for loop:


for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):  # range accepts step
    print(i, end=" ")

for i in range(10, 0, -1):
    print(i)

num = int(input("Enter a number = "))

fact = 1
for a in range(1, num + 1):
    fact = fact * a
print(fact)
