
# number = int(input("Enter a number = "))

# print("checking for even or odd")

# if (number == 0):
#     print("It is zero")
# elif (number % 2 == 1):
#     print("it is an odd number)
# else:
#     print("it is an even number")
    
    
##############################

# num = int(input("enter a number = "))

# print("checking for it's divisiblity")

# if num%2 == 0 and num%3 == 0 and num%8 !=0:
#     print("it is divisible by 2 and 3 not 8")
    
# else:
#     print("invalid number")
    

###########################

# num_check = int(input("Enter number =  "))

# last = num_check%10
# print(last)

# if last%5 == 0:
#     print("Last digit is divisible by 5")
    
# else:
#     print("not divisible by 5")



#######################

# no1 = int(input("Enter number 1 = "))
# no2 = int(input("Enter number 2 = "))
# no3 = int(input("Enter number 3 = "))

# if ( no1 > no2 and no1 > no3):
#     print("no1 is graeter")
# elif ( no2 > no1 and no2 > no3):
#     print("no2 is greater")
# elif ( no3 > no2 and no3 > no1):
#     print("no3 is greater")
# elif( no1 == no2 == no3):
#     print("they are equal")
# else:
#     print("they are not in test")
    
    
####################################

# year = int(input("Enter year = "))

# # this is for years
# if year%4 == 0 and year%100 != 0:
#     print("It is a leap year")

# #this is for century years    
# elif year%100 == 0 and year%400 == 0:
#     print("It is a leap year")
    
# else:
#     print("it is not a leap year")
    
    
######################################

# salary = int(input("Enter your salary = "))

# print("your salary is",salary)

# if salary > 0 and salary < 10000:
#     salary += 0.05*salary
#     print("now your salary is",salary)
    
# elif salary >=10000 and salary <20000:
#     salary += 0.1*salary
#     print("now your salary is",salary)
    
# elif salary >=20000 and salary <50000:
#     salary += 0.15*salary
#     print("now your salary is",salary)
    
# elif salary >=50000:
#     salary += 0.2*salary
#     print("now your salary is",salary)
    
# else:
#     print("salary is invalid")
    
    
    
##################################

num = int(input("Enter a number = "))

if num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
    
elif num%3 == 0:
    print("Fizz")
    
elif num%5 == 0:
    print("Buzz")
    
else:
    print(num)