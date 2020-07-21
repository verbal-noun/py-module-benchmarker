# Importing necessary files 
import math 
import time 
import random
import statistics

def benchmarker(functions, args): 

    # Dictionary to hold the runtime of the comparing functions 
    times = {f.__name__: [] for f in functions}

    A = [64, 25, 12, 22, 11, 50, 19, 34, 35, 53, 55, 54]

    for i in range(3000):
        for _ in range(len(functions)):
            func = random.choice(functions)
            t0 = time.time()
            func(A.copy())
            t1 = time.time()
            times[func.__name__].append((t1-t0)*1000)


    for name, numbers in times.items(): 
        print('FUNCTION:', name, 'Used', len(numbers), 'times')
        print('\tMEDIAN', statistics.median(numbers))
        print('\tMEAN  ', statistics.mean(numbers))
        print('\tSTDEV ', statistics.stdev(numbers))