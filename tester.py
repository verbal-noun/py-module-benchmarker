import tracemalloc

from lib.a_star import * 
from lib.maze.diagrams import * 

def test_func(arg1, arg2):
    result = arg1 * arg2 
    return result
A = [10, 1, 2, 54, 2, 4, 9, 23, 32, 31]
graph = diagram3
start, goal = (1, 4), (38, 28) 

tracemalloc.start()
path = a_star_search(graph, start, goal)
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
tracemalloc.stop()

print(current, peak)