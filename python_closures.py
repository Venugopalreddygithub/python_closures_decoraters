# Closures in python 


# Nested Functions 
# def outer(x):
#     def inner():
#         print(x)
#     inner() 

# outer(3)

# Functions are objects 

# def f():
#     print("hi")
    
# a = f
# print(a)
# print(f)

def outer():
    x = 3 
    def inner():
        y = 3 
        return x + y 
    return inner 

a = outer()
print(a())