import sys
import execution_time_algorithm
import algorithms
#import pygame as pg
#import numpy as np
import matplotlib.pyplot as plt

def plot_execution_time():
    size = []
    time_1 = []
    time_2 = []
    time_3 = []
    time_4 = []
    table = execution_time_algorithm.take_execution_time(10, 100, 100, 10)
    for row in table:
        size.append(row[0])
        time_1.append(row[1])
        time_2.append(row[2])
        time_3.append(row[3])
        time_4.append(row[4])
        print(row)
  
    size = [x for x in size]
    fig, ax = plt.subplots()
    ax.plot(size, time_2, mfc = 'black', marker = '.', ms = 12, color= 'blue', label='python queue',linestyle= '--')  
    ax.plot(size, time_3, mfc = 'black', marker = '.', ms = 12, color= 'orange', label='python deque',linestyle= '--')
    ax.plot(size, time_1, mfc = 'black', marker = '.', ms = 12, color= 'red', label='my queue',linestyle= '--')
    ax.plot(size, time_4, mfc = 'black', marker = '.', ms = 12, color= 'yellow', label='my double linked list',linestyle= '--')
    #plt.show()

    return fig
if __name__ == "__main__":
    chart = plot_execution_time()
    plt.show()
