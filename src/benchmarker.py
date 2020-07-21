# Importing necessary files 
import math 
import time 
import random
import statistics


def benchmarker(functions, args): 

    # Dictionary to hold the runtime of the comparing functions 
    times = {f.__name__: [] for f in functions}

    # Load the arguments to proper functions 
    argument_dict = {}
    for i in range(len(functions)):
        argument_dict[functions[i].__name__] = args[i]
    
    for i in range(3000):
        for _ in range(len(functions)):
            func = random.choice(functions)
            func_args = argument_dict[func.__name__]
            t0 = time.time()
            func(*func_args)
            t1 = time.time()
            times[func.__name__].append((t1-t0)*1000)


    for name, numbers in times.items(): 
        print('FUNCTION:', name, 'Used', len(numbers), 'times')
        print('\tMEDIAN', statistics.median(numbers))
        print('\tMEAN  ', statistics.mean(numbers))
        print('\tSTDEV ', statistics.stdev(numbers))