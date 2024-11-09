# a = [34, 12, 78, 98]

""" 
methods are also function but they are specific to data types
"""
# a.sort()
# print(a)

# # some functions
# print(len(a))
# print(sum(a))
# print(max(a))
# print(min(a))

""" 
adding data methods:
"""
a = [34, 12, 78, 98]
b = []
# append: adds data at end
a.append(100)
# a.append("Parag", 23.5, 56)  # it will only take one argument not more then one
b.append(a[2])
print(a)
print(b)

""" insert method: it will require two argument(<position>,<value>)
 at which position we want to add value, other element will move right
"""
# a.insert(3, "Parag")
# a.insert(500, "python")  # this will add at last
# print(a)


"""
update method:
"""

# a[1] = 2000 # this takes index as a parameter
# a[200] = 100  # this is not possible as index of 200 is not available
# print(a)

"""
deleteing data
"""

# pop: it will delete the element as per index position , by default deletes last element
# remove: it will delete the element as per value ,we have to ass the value

# a.pop()
# a.pop(2)

# a.remove(98) # it will only remove first of same values
# print(a)

# del a[0]
# # del a  # note: del works on any datatype not only on list
# print(a)


# clear: it will empty the list

# a.clear()
# print(a)  # list will be there but without any elements
