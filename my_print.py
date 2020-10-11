'''
AUTHOR
John Park (john-yohan-park)


INSTRUCTIONS
1. put this file in the same directory as your working file
2. import its usable functions: `from my_print import *`


USABLE FUNCTIONS

print_time(func, param 1, param2, ...)
    WHAT IT DOES    print function's result and runtime
                
print_var(some_variable)
    WHAT IT DOES    print variable's name and value  

'''

import time

def now_in_nanosec():
    return int(time.time_ns())

def print_microsec(start_ns, end_ns):
    microsec = (end_ns - start_ns) / 1000
    print(f'{microsec} microsec')

def print_time(*args):
    func_to_run = args[0]
    params = args[1:]

    start = now_in_nanosec()
    res = func_to_run(*params)
    end = now_in_nanosec()

    if res:
        print(res)
    print_microsec(start, end)

import inspect
import re
import collections

def print_dict(var, indent = 0):
    for key, value in var.items():
        if isinstance(value, dict):
            print('  ' * indent + str(key))
            print_dict(value, indent + 1)
        else:
            print('  ' * (indent + 1) + f'{key}: {value}')
    
def print_var(var):
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    var_name = re.search(r'\((.*)\)', s).group(1)
    
    if type(var) is dict or type(var) is collections.defaultdict:
        print(var_name + ': {')
        print_dict(var)
        print('}')

    else:
        print(f'{var_name}: {var}')