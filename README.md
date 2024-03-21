# Homework-4
un deque, una cola (queue), y una pila (stack) son estructuras de datos utilizadas para almacenar elementos y acceder a ellos de diferentes maneras

Deque (doble cola):
Un deque (double-ended queue) es una estructura de datos que permite la inserción y eliminación eficiente de elementos tanto al principio como al final de la secuencia.
Se puede utilizar como una lista, pero con la capacidad de agregar y eliminar elementos eficientemente en ambos extremos.
Se implementa en Python mediante la clase collections.deque.

Cola (queue):
Una cola es una estructura de datos en la que los elementos se agregan al final y se eliminan del principio. Sigue el principio FIFO (First In, First Out).
En Python, puedes usar queue.Queue o queue.deque de la biblioteca estándar para implementar una cola.
Es útil en situaciones donde los elementos deben procesarse en el mismo orden en que se agregaron, como la impresión en cola de trabajos.

Pila (stack):
Una pila es una estructura de datos en la que los elementos se agregan y eliminan del mismo extremo, conocido como la cima (top) de la pila. Sigue el principio LIFO (Last In, First Out).
En Python, puedes usar una lista para implementar una pila o usar collections.deque con métodos específicos como append() y pop() para simular una pila.
Es útil cuando necesitas procesar elementos en el orden inverso al que se agregaron, como en el caso de la inversión de cadenas o la navegación en profundidad en árboles y grafos.
  
La idea de esta tarea es comparar los tiempos de acceso a una posicion en una cola creada nativamente, una cola creada con las builtin functions de python y una lista. 







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