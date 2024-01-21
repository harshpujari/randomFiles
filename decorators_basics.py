# Example of a basic decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()

#dummy outputs 
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

# Decorator with parameters
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")

# Using the decorated function
say_hi("Alice")

#dummy output 2
Hi, Alice!
Hi, Alice!
Hi, Alice!
