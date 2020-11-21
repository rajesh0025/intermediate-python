#decorator:its a fuction that takes another fuction as argumets and extends its behaviour without modifying 
def start_end_decorator(func):#D-function

#function decorators    

    def wrapper():#sub function
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator
def print_name():#fuction that uses D-functon
    print('Alex') 

print_name()

#to give argumenst to D-function
def start_end_decorator(func):#D-function

    def wrapper(*args,**kwargs):#sub function
        print('start')
        result=func(*args,**kwargs)
        print('end')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5
result=add5(10)
print(result)    


import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(num_times):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=5) 
def greet(name):
    print(f"hello {name}")

greet('candice')    

#class--decorators

class Countcalls:

    def __init__(self,func):
        self.func=func 
        self.num_calls=0
    def __call__(self,*args,**kwargs):
        self.num_calls+=1
        print(f'This is executed{self.num_calls} times')
        return self.func(*args,**kwargs)

@Countcalls
def say_hello():
    print("hello")

say_hello()
say_hello()    