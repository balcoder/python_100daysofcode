inputs = eval(input())

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned {function(*args)}")
    return wrapper

@logging_decorator
def a_function(a,b,c):
    return a * b * c

a_function(inputs[0], inputs[1], inputs[2])