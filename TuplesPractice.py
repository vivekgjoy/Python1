# practice with tuples

# tuples are ordered
# tuples are unchangeable
# tuples not allowed duplicates

tup1=(4,2,3,8,7,7)
print(tup1)
print(type(tup1))
tup2=("cat","dog","rat","tom","tree","flower")
print(tup2)
# based on index from tup2
print(tup2[1])
print(tup2[-1])
print(tup2[1:3])
x=list(tup2)

x.append("append")
print(x)

x.append('append')
print(x)

print(tup2.count("dog"))
print(tup2.__hash__())
print(tup2.__len__())
