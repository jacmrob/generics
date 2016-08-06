import sys, os 
import numpy as np 

class Stack:
	'''
	Stack class implemented using a python list
	pop returns None if the stack is empty
	'''
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop() if not self.isEmpty() else None

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items())


class Queue:
	'''
	Queue class implemented using a python list
	dequeue returns None if the stack is empty
	'''
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0) if not self.isEmpty() else None 

	def size(self):
		return len(self.items())


class Node:
	def __init__(self, parent, children, data):
		self.parent = parent
		self.children = children 
		self.data = data 



def dfs(G, r):
	s = Stack()
	s.push(r)
	visited = []
	while s:
		v = s.pop()
		if v not in visited:
			visited.append(v)
			for child in v.children:
				s.push(child)

def bfs(G, r):
	q = Queue()
	q.enqueue(r)
	visited = []
	while q:
		v = q.dequeue()
		if v not in visited:
			visited.append(v)
			for child in v.children:
				q.enqueue(child)


def pre_order(node, order):
	order = []
	order.append(root)
	if root.children[0]:
		pre_order(root.children[0], order)
	if root.children[1]: 
		pre_order(root.children[0], order)

	return order 

def atoi(s):
	sign = 1
	total = 0

	for c in s:
		if c == '-':
			sign = -1 
		else:
			total = total * 10 + int(c)

	return total * sign 

def get_max_profit(prices):
	best_delta = 0
	lowest = prices[0]

	for p in prices[1:]:
		lowest = min(p, lowest)
		best_delta = max(best_delta, p - lowest)

	return best_delta


def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)


def binary_search(array, x):
	if len(array) <= 1:
		return array[0] == x 

	mid = len(array) / 2

	if x > array[mid]:
		return binary_search(array[mid:], x)
	elif x < array[mid]:
		return binary_search(array[:mid], x)
	else:
		return True 



if __name__ == '__main__':

	prices = [10, 7, 5, 8, 11, 9]
	descending = [10, 9, 8, 7, 6]
	#print get_max_profit(prices)
	#print get_max_profit(descending)

	print binary_search(sorted(prices), 20)

