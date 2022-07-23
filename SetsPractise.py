# practice with tuples

# sets are un-ordered
# sets are changeable
# sets not allowed duplicates

# List use curly braces
set = {"abc",'abc',2,45,False}
print(set)

# Access set using in keyword
print("abc" in set)

# Using for loop
for i in set:
    print(i)

# for add a item
set2={7,8,9,10}
set2.add(5)
print(set2)

# union method
set3={"a","v",'s',3,4,5}
set3=set3.union(set2)
print("set3 is",set3)

# Remove method using element
set3.remove("a")
print(set3)

# Discard method doing same like remove method doubt
set3.discard("s")
print(set3)

#pop method
set4={"l",'m',3,4,5,6}
set4.pop()
print(set4)

# intersection will retain common elements

set5=set4.intersection(set3)
print(set5)

# difference elements will be retain between both list
set6={1,2,3,4,5}
set7={1,4,6,8,10}
set8=set6.difference(set7)
print(set8)
print(set6.isdisjoint(set7))

# clear method will clear all elements
set8.clear()
print(set8)

# copy method will copy of existing set elements to new set
set9=set7.copy()
print(set9)

