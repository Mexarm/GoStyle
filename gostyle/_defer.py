from functools import wraps
import inspect

def defer_inside(f):
    @wraps(f)
    def wrapper(*args, **kargs):
        ret_val = f(*args, **kargs)
        locals()["defer_func"]() # Run
        return ret_val
    return wrapper

def defer(*args):
    def defer_runner():
        for func in args:
            func()
    stack = inspect.stack()
    inspect.getargvalues(stack[ 2 ].frame).locals["defer_func"] = defer_runner
