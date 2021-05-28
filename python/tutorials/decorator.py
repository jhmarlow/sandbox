"""decorator test."""
import functools
import sys

def do_twice(func):
    """function."""
    @functools.wraps(func)  # use this to aid with debugging (gives you the funcs doc)
    def wrapper_do_twice():
        """wrapper to return object to be called
        by decorator."""
        func()
        func()
    return wrapper_do_twice


@do_twice
def printer():
    """the function to be called into decorator."""
    print("test")

print(printer.__doc__)
printer()

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice

# @do_twice
# def greet(name, surname):
#     print(f"Hello {name},{surname}")

# greet("jacob", "marlow")