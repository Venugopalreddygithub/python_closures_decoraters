# 1. Multiple Decoraters 

def split(func):
    def wrapper():
        result = func()
        return result.split()
    return wrapper 

def upper_d(func):
    def inner():
        result = func()
        return result.upper()
    return inner 

@split
@upper_d
def ordinary():
    return "good morning!"


print(ordinary())

# 2. If a decorater containers parameters

def outer(exp):
    def decorater(func):
        def inner():
            result = func() + exp 
            return result 
        return inner 
    return decorater  


@outer("amulya")
def ordinary():
    return "good morning!"

print(ordinary())

# 3. multiple function names 


def decorater(func):
    def inner(*args):
        list_a = list(args[1:])
        print(list_a)
        for i in list_a:
            if i == 0:
                return "Enter Valid input"
        return func(*args)
    return inner 

@decorater
def div1(a, b):
    return a / b 
@decorater
def div2(a, b, c):
    return a / b / c 

print(div1(2, 3))
print(div2(3, 2, 0))











