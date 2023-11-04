import time

current_time = time.time()
print(f"The time since Jan 1st 1970 is {current_time}")

def speed_calc_decorator(function):
   def wrapper_function():
       start_time = time.time()
       function()
       end_time = time.time()
       print(f"The {function.__name__} speed was {end_time - start_time}s")
   return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    
fast_function()
slow_function()
