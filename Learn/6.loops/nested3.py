"""
@ @ @ @ *
@ @ @ * *
@ @ * * *
@ * * * *
* * * * *
"""

# for i in range(1,6):
#     for j in range(i ,5): # this for printing the trailing space
#         print(" ", end = " ")
#     for k in range(1,i+1): # this for printing i
#         print("*",end = " ")
#     print()

#########################

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end = " ")
#     for k in range(1,i+1):
#         print(k,end = " ")
#     print()

#############################
"""
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
# for i in range (1,6):
#     for j in range(i,5):
#         print(" ",end = " ")
#     for k in range(1,i+1):
#         print(i,end =" ")
#     print()

##############################

"""
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end =" ")
#     for k in range(1,2*i):
#         print("*",end = " ")
#     print()


###################
"""
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end = " ")
#     for k in range(1,2*i):
#         print("*",end =" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(i,5):
#         print(" ",end = " ")
#     for k in range(1,2*i):
#         print("*",end = " ")
#     print()


"""
@ @ @ @ *
@ @ @ * *
@ @ * * *
@ * * * *
* * * * *
"""


# def pattern(n):

#     for i in range(1, n + 1):
#         for j in range(i, n):
#             print(" ", end=" ")
#         for k in range(1, i + 1):
#             print("*", end=" ")
#         print()


# pattern(5)

"""
       1
     2 2
   
   
5 5 5 5 5   
"""


# def pattern(n):

#     for i in range(1, n + 1):
#         for j in range(i, n):
#             print(" ", end=" ")
#         for k in range(1, i + 1):
#             print(i, end=" ")
#         print()


# pattern(5)

"""
         5
       4 5
       
       
  1 2 3 4 5
"""

# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for k in range(i, 6):
#         print(k, end=" ")
#     print()


"""
        * 
      * * *
    * * * * *
  * * * * * * *
"""

# for i in range(1, 6):
#     for k in range(i, 5):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print("*", end=" ")
#     print()


"""
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

# for i in range(1, 6):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
# for i in range(4, 0, -1):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()

# Hard Pattern
"""
       1
     2 1
   
   
5 4 3 2 1     
"""

# for i in range(1, 6):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for k in range(i, 0, -1):
#         print(k, end=" ")
#     print()

"""

"""
# for i in range(1, 6):
#     for k in range(i, 5):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(i, end=" ")
#     print()


"""

"""
# for i in range(1, 6):
#     for k in range(i, 5):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print(j, end=" ")
#     print()

"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5


"""

# for i in range(5, 0, -1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()
# for i in range(2, 6):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()


"""
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
"""

# for i in range(5, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()


"""

"""

# for i in range(1, 6):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for k in range(1, 5):
#         print("*", end=" ")
#     print()

"""

"""

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
for i in range(1, 5):
    for j in range(i, 4):
        print(" ", end=" ")
    for k in range(0, 2 * i + 1):
        print("*", end=" ")
    print()
