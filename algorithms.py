# Queue created from scratch 
# Double linked list implementation : https://www.youtube.com/watch?v=Wf4QhpdVFQo 
import queue
from collections import deque

#Double linked list implementation

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int :
        cur = self.left.next
        while cur and index > 0: 
            cur = cur.next
            index -= 1
        if cur and index ==0 and cur != self.right:
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node, nextt, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        nextt.prev = node
        node.next = nextt
        node.prev = prev
    
    def addAtTail(self, val : int) -> None: 
        node, nextt, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        nextt.prev = node
        node.next = nextt
        node.prev = prev
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= -1
        if cur and index == 0: 
            node, nextt, prev = ListNode(val), cur , cur.prev
            prev.next = node
            nextt.prev = node
            node.next = nextt
            node.prev = prev
    def deleteAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= -1
        if cur and cur != self.right and index == 0: 
            nextt, prev = cur.next , cur.prev
            nextt.prev = prev
            prev.next = nextt
    def print_list(self):
        cur = self.left.next
        while cur:
            print(cur.val)
            cur = cur.next

# Queue created from scratch 
class my_queue_from_0:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def empty(self):
         return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            raise IndexError ("The Queue is empty")
    def peek(self):
        if not self.empty():
            return self.items[0]
        else:
            raise IndexError ("The Queue is empty")
 
def my_queue(items):
    #Queue creation
    my_queue = my_queue_from_0()
    for x in items:
        my_queue.enqueue(x)
    return my_queue
# item get from my queue
def get_item_my_queue(my_q, target):
    #my_q = my_queue(items)
    for x in range(0,target-1):
        my_q.dequeue()
    return my_q.peek()
# Creation of queues from python class

def python_queue(items):
    py_queue = queue.Queue()
    for x in items:
        py_queue.put(x)
    return py_queue
# item get  from python queue

def get_item_python_queue(py_q, target):
    #py_q = python_queue(items)      
    for x in range(0, target-1):
        py_q.get()

    return py_q.get()
        
#Creation of deques from python class

def python_deque(items):
    py_deque = deque()
    for x in items:
        py_deque.append(x)
    return py_deque

# Item get from python deque
def get_item_python_deque(dq,target):
    #dq = python_deque(items)
    if target <= len(dq)//2:
        for i in range(0,target-1):
            dq.popleft()
        return dq.popleft()
    elif target > len (dq)//2:
        for i in range(target,len(dq)):
            dq.pop()
        return dq.pop() 
    
# Double linked list creation
def my_double_linked_list(items):
    my_list = MyLinkedList()
    for x in items:
        my_list.addAtTail(x)
    #my_list.print_list()
    return my_list 

def get_item_double_linked_list(my_dlist, target):
    idx_get = my_dlist.get(target)
    return idx_get
'''
items = [1,2,3,4,5,6,7,8,9,10,11,12,30,15,16]
myqueue = my_queue(items)
print(myqueue)
print(get_item_my_queue(myqueue,3))
#print(get_item_double_linked_list(items, 2))
'''

#if __name__ == "main":
    #items = [1,2,3,4,5,6,7,8,9,10,11,12,30,15,16]
    #my_list = MyLinkedList()
    #for x in items:
        #my_list.addAtHead(x)
    #MyLinkedList.print_list()

