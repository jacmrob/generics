import sys, os 
import numpy as np 


## Custon data structures 

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
	'''
	Hash table implemented using python lists
	valid key types are strs and ints 
	utilizes a universal hash function w/ prime > size of set to hash (n)
	Insert: O(1), Delete: O(1), lookup O(1)
	space complexity O(n)
	'''
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
		elif type(key) is int:
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
			if k == key:
				return v 
		raise StandardError("Key Error!  Key not found.") 

	def delete(self, key):
		index = self.hashf(key)
		for i, (k,v,o) in enumerate(self.table[index]):
			if k == key:
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


## Trees and tree traversals 

class Node:
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None 


class BinaryTree:
	'''
	Implementation of a binary tree with numeric data
	Insert: O(logn) if balanced, O(n) worst case
	Delete: O(logn) if balanced, O(n) worst case
	Lookup: O(logn) if balanced, O(n) worst case
	Space complexity O(n)
	'''

	def __init__(self):
		self.node = None
		self.height = -1 

	def insert(self, data):
		if not self.node:
			self.node = Node(data)
			self.node.left = BinaryTree()
			self.node.right = BinaryTree() 

		elif data < self.node.data:
			self.node.left.insert(data)

		elif data > self.node.data:
			self.node.right.insert(data)

		else:
			raise StandardError("Node already in tree")

		# update height of subtree 
		self.height = max(self.node.left.height, self.node.right.height) + 1 

	def search(self, data):
		if data == self.node.data:
			return True 
		elif data < self.data:
			self.node.left.search(data)
		elif data > self.data:
			self.node.right.search(data)
		return False 

	def get_height(self):
		return self.height 

	def is_complete(self):
		pass
		# todo


def dfs(tree):
	# O(n)
	s = Stack()
	visited = []
	if tree.node:
		s.push(tree.node)
	while not s.isEmpty():
		n = s.pop()
		if n and n not in visited:
			visited.append(n.data)
			if n.left.node:
				s.push(n.left.node)
			if n.right.node:
				s.push(n.right.node)

	return visited

def bfs(tree):
	# O(n)
	q = Queue()
	visited = []
	if tree.node:
		q.enqueue(tree.node)
	while not q.isEmpty():
		 n = q.dequeue()
		 if n and n not in visited:
		 	visited.append(n.data)
		 	if n.left.node:
		 		q.enqueue(n.left.node)
		 	if n.right.node:
		 		q.enqueue(n.right.node)
	return visited

def pre_order(tree, order=[]):
	if tree.node:
		order.append(tree.node.data)
		if tree.node.left:
			pre_order(tree.node.left, order)
		if tree.node.right: 
			pre_order(tree.node.right, order)
	return order 

def post_order(tree, order=[]):
	if tree.node:
		if tree.node.left:
			post_order(tree.node.left, order)
		if tree.node.right:
			post_order(tree.node.right, order)
		order.append(tree.node.data)
	return order 

def in_order(tree, order=[]):
	if tree.node:
		if tree.node.left:
			in_order(tree.node.left, order)
		order.append(tree.node.data)
		if tree.node.right:
			in_order(tree.node.right, order)
	return order 


# misc algorithms

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

	#print binary_search(sorted(prices), 20)

	

