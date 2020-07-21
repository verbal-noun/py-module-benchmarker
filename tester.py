from src.benchmarker import benchmarker
from lib.sorting import *

# List the name of functions we want to compare 
functions = bubbleSort, selectionSort, insertionSort

# List the arguments we want to pass into each function 
# NOTE - the ORDER of the functions above and arguments you put here MUST MATCH! 
A = [64, 25, 12, 22, 11, 50, 19, 34, 35, 53, 55, 54]
args = [[A.copy()], [A.copy()], [A.copy()]]


benchmarker(functions, args)
