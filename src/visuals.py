from src.benchmarker import benchmarker 
import statistics
import matplotlib.pyplot as plt 
import numpy as np 

def visualizer(time_stats, memory_stats, functions): 
    
    # Converting to appropriate data 
    func_names = []
    performance = []
    error = []
    peak_memory = []

    for name, number in time_stats.items():
        func_names.append(name)
        performance.append(statistics.mean(number))
        error.append(statistics.stdev(number))
        peak_memory.append(memory_stats[name])

    y_pos = np.arange(len(func_names))

    # Plotting the runtime performance 
    fig1 = plt.figure(figsize=(10,10))
    ax1 = fig1.add_subplot()

    ax1.barh(y_pos, performance, xerr=error, align='center', 
             color='green', ecolor='black')
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(func_names)
    # Read labels top to bottom 
    ax1.invert_yaxis()
    # Labels 
    ax1.set_xlabel('Mean Runtime (ms)')
    ax1.set_title('Runtime Comparison')
    


    # Plotting the memory performance 
    fig2 = plt.figure(figsize=(10,10))
    ax2 =  fig2.add_subplot()

    ax2.barh(y_pos, peak_memory, align='center')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(func_names)
    #Read labels top to bottom 
    ax2.invert_yaxis()
    # Labels 
    ax2.set_xlabel('Peak Memory Use (KB)')
    ax2.set_title('Memory Usage Comparison')
    
    # Show the plot 
    plt.show()