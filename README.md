# **Project Title: Data Structure Performance Comparison**

## **Introduction**
Welcome to the project repository for comparing the performance of different data structures! This project focuses on comparing the access times of various data structures implemented natively versus those provided by the Python library. Specifically, implementations of a queue and a doubly linked list were created from scratch, alongside using Python's built-in Queue and Deque classes. The objective is to measure the time taken to access elements within each data structure and analyze their efficiency.

## **Objective**
The primary objective of this project is to evaluate and compare the performance of different data structures when accessing elements. By conducting performance tests on custom implementations of a queue and a doubly linked list, as well as using Python's built-in Queue and Deque classes, we aim to understand the trade-offs and efficiencies of each approach.

## **Implementation Details**
The project involves the following steps:

### **Data Structure Implementations:***

Native implementation of a queue and a doubly linked list.
Utilization of Python's built-in Queue and Deque classes.
Performance Testing:

Iteratively varying the size of the input list from i to j elements, incrementing by m in each iteration.
For each list size, searching for q number of items.
Recording and summing the access times for searching q items in each list size.
Data Analysis:

Analyzing the total access times for each data structure at different list sizes.
Plotting the execution time against the list size to visualize performance trends.
Usage
## **To run the performance comparison program, follow these steps:**

Clone the repository from GitHub: git clone https://github.com/juan-aguilera/Homework-4.git
Navigate to the project directory: cd data-structure-performance
Run the performance comparison script: python performance_comparison.py
Analyze the generated plots to observe the performance of each data structure.
## **Results**
The project generates graphical representations of the execution time versus the list size for each data structure. By analyzing these results, insights into the performance characteristics of different data structures can be gained, aiding in informed decision-making regarding their usage in various scenarios.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or assistance, feel free to contact the project maintainer:

Name: [Juan Esteban Aguilera]
Email: [juanestebangamba333@gmail.com]
Thank you for exploring our data structure performance comparison project! We hope it provides valuable insights into optimizing algorithmic efficiency.

COVERAGE: 
Name                          Stmts   Miss  Cover
-------------------------------------------------
algorithms.py                    71      8    89%
constants.py                      2      0   100%
data_generator.py                10      0   100%
execution_time_algorithm.py      24      0   100%
running_file.py                  27      0   100%
-------------------------------------------------
TOTAL                           134      8    94%
