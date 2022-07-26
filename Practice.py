# print ("sub", a-b)
# print ("multi", a*b)
# print ("div", a/b)

# shorthand

a=10
b=20
c=30

if a<b: print ("a is greater")

print ("Both conditions ar true") if b>a and c>a \
    else print ("conditions are failed")

# using pass keyword
if a<b:
    pass
    print (a)

i=0
while i<6:
    print (i)
    print("Hello all")
    if (i==3):
        print ("Completed....")
        break
    i=i+1

# using continue keyword

i=1
while i<10:
    i=i+1
    if(i==5):
        print("skip")
        continue
    print ("num",i)

# using break keyword
i=0
while i<5:
    print(i)
    print("hello all")
    if(i==3):
        break
    i=i+1
else:
    print("Process completed")

# python functions

def func(a1,a2):
    print(a1+a2)
func (3,4)

def family(*childs):
    for x in childs:
        print(x)
family ("vivek", "vignesh", "ramu")


def relation (c3,c2,c1):
    print(c2, "is our relation")
relation (c3="vivek", c2="vignesh", c1="ramu")


def family(**kids):
    print("2nd child:"+kids["c2"])
family (c1="karthik", c2="velan", c3="arun",c4="kiran")


# lamda expression
# syntax
# lamda argument : expression

x=lambda a,b,c : print (a+b+c)
x(5,10,15)
