import time

# Write your code below 👇

def speed_calc_decorator(function):
    
    def wrapper_func():
        before_call_time= time.time()
        function()
        after_call_time= time.time()
        print(after_call_time-before_call_time)
        
    return wrapper_func    

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(19000000):
    i * i

slow_function()
fast_function()
