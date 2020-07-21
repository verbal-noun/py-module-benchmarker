from src.benchmarker import benchmarker
from lib.a_star import *
from lib.a_star_variants import * 
from lib.maze.diagrams import diagram3

# List the name of functions we want to compare 
functions = a_star_search, weighted_a_star, bidirectional_a_star

# List the arguments we want to pass into each function 
# NOTE - the ORDER of the functions above and arguments you put here MUST MATCH! 
A = [64, 25, 12, 22, 11, 50, 19, 34, 35, 53, 55, 54]
start, goal = (1, 4), (38, 28)
args = [[diagram3, start, goal], 
        [diagram3, start, goal], 
        [diagram3, start, goal]]


benchmarker(functions, args)
