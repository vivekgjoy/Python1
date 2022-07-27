# function as a argument to another function
# function inside a function
# store function in a var
# function as a object

# decorators
# takes function, add functionality and returns functions
# without didturbing the main function
# metaprogramming

def func():
    return "Hello"

print(func())

assign = func
print("assigned var", assign())

def name(text):
    return "Hello "+text.upper()
print(name("Vivek"))

# function as a argument

def nmae(text):
    return text.title()
    #name
def main_func(func):
    #name
    result = func("hello all...")
    print(result)
main_func(name)

def name(text):

    if "p" in text:
        return "welcome " +text
    else:
        return "Not allowed"

def allow(func):
    result = func("Vivek")
    print(result)

# allow (name)
# inner function
# nested function
# inner function can access all variables defined in outer functon

def outer_func():
    def inner_func():
        print("hello")

    inner_func()

outer_func()

def outer_func(name):
    text = "are you"
    def inner_func():
        print("How "+text)
    inner_func()
outer_func("arun")

def sub(a,b):
    if(a<b):
        a,b=b,a
    print(a-b)

sub (10,20)

def dec_func(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        return inner
sub(8,5)


