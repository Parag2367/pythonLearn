"""
1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5
"""

# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

######################

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end = " ")
#     print()

#############################

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

# for i in range (1,6):
#     for j in range(i,0,-1):
#         print(j,end = " ")
#     print()

##############################
"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end =" ")
#     print()

####################

"""
5
4 4 
3 3 3 
2 2 2 2
1 1 1 1 1
"""

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i,end = " ")
#     print()


"""
*
* *
* * *
* * * *
* * * * *
"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()

###################

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end = " ")
#     print()

############################

"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

# for i in range (5,0,-1):
#     for j in range(1,i+1):
#         print(i,end = " ")
#     print()

#######################

"""
* * * * *
* * * *
* * *
* *
*
"""

# for i in range (1,6):
#     for j in range (5,i-1,-1):
#         print("*",end = " ")
#     print()

####################

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

# for i in range (5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end = " ")
#     print()

######################

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

##################

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

# count = 0
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         count = count + 1
#         print(count, end=" ")
#     print()


"""
1 2 1 2 1
1 2 1 2
1 2 1
 1 2
 1
"""

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(2, end=" ")
#         else:
#             print(1, end=" ")
#     print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
count = 0
for i in range(1, 6):
    for j in range(1, i + 1):
        count = count + 1
        print(count, end=" ")
    print()
