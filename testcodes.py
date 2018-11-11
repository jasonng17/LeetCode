#!/usr/bin/env python3
"""
@author: darklord
"""

'''
Rotate 2D matrix by 90 degrees
'''
from copy import deepcopy
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

A = [[1,2],
     [3,4]]

#results = deepcopy(A)
n = len(A)
for x in range(0,n):
    for y in range(n-1,-1,-1):
        A[y][n-x-1] = A[x][y]


'''
Implement a LRU cache
1. Create node
2. Create LRU
3. Operations
    - Get a value (Check if present, true update, false return -1)
    - Set a value (Check if present, true remove because we want to refresh, 
                   Create a new node and insert to tail
                   Check if within capacity, else drop from head)
4. Create helper functions to easily add or remove
'''

cache = cacheLRU(2)
cache.set(1,10)
cache.set(5,12)
cache.get(5)
cache.get(1)
cache.get(10)
cache.set(6,14)
cache.get(5)

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class cacheLRU():
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # add to tail
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
    
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1
        
    def set(self, key, value):
        if key in self.dict: self._remove(dict[key])
        node = Node(key, value)
        self._add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            # select node to remove
            node = self.head.next
            print("pushing out key {} and value {}".format(node.key, node.value))
            # Remove node from linked list and dict
            self._remove(node)
            del self.dict[node.key]

































