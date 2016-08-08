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

class HashTable:
	def __init__(self, n):
		self.prime = self.get_next_prime(n)
		self.table = [[] for i in range(self.prime)]  
		self.keys = []
		self.values = []
		self.order_id = 0

	def hashf(self, key):
		# hash function for str or int keys
		if type(key) is str:
			return hash(key) % self.prime 
		else if type(key) is int:
			return key % self.prime
		else:
			raise StandardError("Key is not a valid type! Must be string or int.")


	def insert(self, key, value):
		index = self.hashf(key)
		self.table[index].append((key, value, self.order_id))
		self.keys.append(key)
		self.values.append(value)
		self.order_id += 1 

	def get(self, key):
		index = self.hashf(key)
		for (k,v,_) in self.table[index]:
			if k = key:
				return v 
		raise StandardError("Key Error!  Key not found.") 

	def delete(self, key):
		index = self.hashf(key)
		for i, (k,v,o) in enumerate(self.table[index]):
			if k = key:
				remove_index = i 
				order_index = o 
				break 
			raise StandardError("Key Error! Key not found.")
		del self.table[index][remove_index]
		del self.keys[order_index]
		del self.values[order_index]
		 

	def get_keys(self):
		return self.keys

	def get_values(self):
		return self.values

	def get_next_prime(self, n):
		while not self.is_prime(n):
			n += 1
		return n 

	def is_prime(self, n):
		for i in range(2,int(n**0.5)+1):
			if n % i == 0:
				return False
		return True 


# todo: implement this better for binary tree
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
	order.append(node)
	if node.children[0]:
		pre_order(node.children[0], order)
	if node.children[1]: 
		pre_order(node.children[0], order)

	return order 

def post_order(node, order):
	if node.children[0]:
		post_order(node.children[0], order)
	if node.children[1]:
		post_order(node.children[1], order)
	order.append(node)
	return order 

def in_order(node, order):
	if node.children[0]:
		in_order(node.children[0], order)
	order.append(node)
	if node.children[1]:
		in_order(node.children[1], order)
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

	root = Node()

