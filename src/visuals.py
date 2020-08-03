from src.benchmarker import benchmarker 
import statistics
import matplotlib.pyplot as plt 
import numpy as np 

def visualizer(time_stats, memory_stats, functions): 
    # Converting to appropriate data 
    func_names = []
    performance = []
    error = []

    for name, number in time_stats.items():
        func_names.append(name)
        performance.append(statistics.mean(number))
        error.append(statistics.stdev(number))

    y_pos = np.arange(len(func_names))

    # Drawing the bar charts 
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.barh(y_pos, performance, xerr=error, align='center', 
             color='green', ecolor='black')
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(func_names)
    # Read labels top to bottom 
    ax1.invert_yaxis()
    # Labels 
    ax1.set_xlabel('Mean Runtime')
    ax1.set_title('Runtime Comparison')
    plt.show()