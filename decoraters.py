# Decoraters 

# 1.string to uppercase 


def outer(func):
    def inner():
        result = func()
        return result.upper()
    return inner 

@outer
def print_str():
    return "good morning!"

print(print_str())

# 2.Division - passing parameters to the function

def div_decorater(func):
    def inner(a, b):
        if b == 0:
            return "Enter valid input"
        return func(a, b)
    return inner 

@div_decorater 
def div(a, b):
    return a / b 

print(div(4, 0))


