
import time
import algorithms
import constants
import data_generator
import copy
import queue
from collections import deque 
def take_execution_time(initial_size, final_size, step,qty):
    return_table = []
    my_queues, py_queues, py_deques, my_dlinked_lists, targets = data_structures_generation(initial_size,final_size,step)
    #print(my_queues)
    for size in range(initial_size, final_size, step):
        table_row = [size]
        times = take_times(my_queues.get(size),py_queues.get(size),py_deques.get(size),my_dlinked_lists.get(size),qty,targets.get(size))
        return_table.append(table_row + times)
        #print(times)

    return return_table

def take_times(my_queue, py_queue, py_deque, my_dlinked_list,qty,targets):
    return [
        #take_time_for_python_queue(clone_python_queue(sample), algorithms.python_queue),
        #take_time_for_my_queue(clone_my_queue(sample), algorithms.python_queue),
        take_time_for_algorithm(my_queue, algorithms.get_item_my_queue,qty,targets,"myqueue"),
        take_time_for_algorithm(py_queue, algorithms.get_item_python_queue,qty,targets,"pyqueue"),
        take_time_for_algorithm(py_deque, algorithms.get_item_python_deque,qty,targets,"pydeque"),
        take_time_for_algorithm(my_dlinked_list, algorithms.get_item_double_linked_list,qty,targets,"my dlinked list")
    ]
#abstraccion, hererencia e inversion de dependencias

def take_time_for_algorithm(data_structure_sample,data_structure_algorithm,qty,targets,type):
    times = []
    cnt = 0
    for i in range(0, qty):
        cnt += 1
        print(cnt)
        if type == "myqueue":
            a = clone_my_queue(data_structure_sample)
        elif type == "pyqueue":
            a = clone_py_queue(data_structure_sample)
        elif type == "pydeque":
            a = clone_py_deque(data_structure_sample)
        elif type == "my dlinked list":
            a = clone_dlinked_list(data_structure_sample)
        #print(a)
        start_time = time.perf_counter_ns()
        data_structure_algorithm(a,targets[i]) 
        times.append(int(constants.TIME_MULTIPLIER * (time.perf_counter_ns() - start_time)))
    #print(times)
    times.sort()
    return times[len(times) // 2]

def data_structures_generation(ini_size,final_size,step):
    my_queues = {}
    py_queues = {}
    py_deques = {}
    my_dlinked_lists = {}
    targets = {}
    for i in range (ini_size,final_size + 1,step):
        items = data_generator.list_gen(i)
        my_queues[i] = algorithms.my_queue(items)
        py_queues[i] = algorithms.python_queue(items)
        py_deques[i] = algorithms.python_deque(items)
        my_dlinked_lists[i] = algorithms.my_double_linked_list(items)
        targets[i] = data_generator.target_gen(i) 
    return my_queues, py_queues, py_deques, my_dlinked_lists, targets

'''
my_queues, py_queues, py_deques, my_dlinked_lists, targets = data_structures_generation(10,100,10)
for i in range(10,100,10):
    print(my_queues.get(i))
'''
def clone_my_queue(my_queue):
    my_queue_cloned = copy.deepcopy(my_queue)
    return my_queue_cloned
def clone_py_queue(py_queue):
    py_queue_cloned = queue.Queue()
    for items in list(py_queue.queue):
        py_queue_cloned.put(items)
    return py_queue_cloned
def clone_py_deque(py_deque):
    py_deque_cloned = deque(copy.deepcopy(py_deque))
    return py_deque_cloned
def clone_dlinked_list(my_dlinked_list):
    dlinked_list_cloned = copy.deepcopy(my_dlinked_list)
    return dlinked_list_cloned