# Dictionaries are ordered
# not accept duplicates
# Dictionaries are changeable

# dictionary sample
d={"name":"vivek","age":"25","percentage":"70.5"}
print (d["name"])

# get we can print key value pairs
print(d.get("age"))

# for get all key & values
x=d.keys()
y=d.values()
print(x)
print(y)

# for get all items
z=d.items()
print(z)

# for change value of pair
d["name"]="vignesh"
d["age"]="26"
d["percentage"]="75.0"
print(d)

# change using update
d["name"]="vinay"
print(d)

# delete using pop method
d.pop("percentage")
print(d)

# delete last entry using popitem method
d.popitem()
print(d)

# using del method doubt
# k={"s":1,"t":2}
# del k
# print(k)

# clear
s={"name":"arun", "class":12, "age":17}
s.clear()
print(s)

# using copy we can get same dictionary
w={"name":"arun", "class":12, "age":17}
e=w.copy()
print(w)
print(e)

#using in keyword
f="name" in e.keys()
print(f)

f="arun" in e.values()
print(f)

# doubt
for x,y in e.items():
    print("items i in e",x,y)

# nested dictionaries
family = {
    "mother" : {"name":"yazhini", "age":35},
    "son1" : {"name":"ramesh", "age":14},
    "son2" : {"name":"kiran", "age":17}
}
# doubt
# print(family)
# "mother" : {"name":"yazhini", "age":50}
# "son1" : {"name":"ramesh", "age":14}
# "son2" : {"name":"kiran", "age":17}









