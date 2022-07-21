
# today we will practice about list

a=["hi","Hello",'vivek', 'v', "h",6]
print(a)
b=["hi","Hello",'vivek', 'v', "h"]
print(b)

# after append
b.extend(["juice"])
print(b)

# after reverse
print(b.reverse())
print(b)

# after pop
b.pop(3)
print(b)

# after insert
b.insert(2,"vivek")
print(b)

# after contains method
c=b.__contains__("vivek")
print(c)

# list size is doubt
d=b.__sizeof__()
print(d)

# list length is
print(len(b))

# type of list
print(type(b))

# present not present
print("lemon" in b)
print("lemon" not in b)

# after insert list will be
b.insert(2, "orange")
print(b)

# after remove the item
b.remove("orange")
print(b)

# joining 2 list
b=b+a
print(b)

# reverse of list
b.reverse()
print(b)

# removal of element
b.remove(6)
print(b)

# removal of element
b.sort()
print(b)

# after clear
print(b.clear())
print(b)

