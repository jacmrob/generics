from __future__ import division
import numpy as np 
import random
from collections import defaultdict 
import math 

from generics import Queue

def selection_sort(array):
	# average O(n^2)
	# worst case O(n^2)
	# O(1) space complexity (in-place)
	s = []
	for i in range(len(array)):
		m = min(array)
		array.remove(m)
		s.append(m)

	return s 


def insertion_sort(array):
	# average O(n^2)
	# worst O(n^2)
	# O(1) space complexity (in-place)

	for i in range(len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j = j-1 
	return array 


def merge_sort(array):
	# average O(nlog(n))
	# worst O(nlog(n))
	# O(n) space complexity 

	n = len(array)
	if n <= 1:
		return array

	mid = n / 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])

	def _merge(a, b):
		 result = []
		 a_ind = 0
		 b_ind = 0
		 while a_ind < len(a) and b_ind < len(b):
		 	if a[a_ind] <= b[b_ind]:
		 		result.append(a[a_ind])
		 		a_ind += 1
		 	else:
		 		result.append(b[b_ind])
		 		b_ind += 1
		 if a_ind < len(a):
		 	result += a[a_ind:]
		 if b_ind < len(b):
		 	result += b[b_ind:]
		 return result

	return _merge(left, right) 


def quick_sort(array):
	# average O(nlog(n))
	# worst O(n^2)  (if pick worst pivot every time)
	# O(logn) space complexity

	n = len(array)
	if n <= 1:
		return array 

	pivot = array[random.randint(0, n-1)]
	l, e, g = [], [], []
	for x in array:
		if x < pivot:
			l.append(x)
		elif x > pivot:
			g.append(x)
		else:
			e.append(x)
	return quick_sort(l) + e + quick_sort(g)


def radix_sort(array):
	# average O(nk)  (where k is max # digits)
	# worst O(nk)
	# space O(n+k)
	# only for positive numbers 

	def concat_buckets(b):
		c = []
		for i in range(9):
			if b.get(i):
				c += b.get(i)
		return c 

	max_digits = 1
	def digits(n):
		if n != 0:
			return int(math.log10(n)) + 1 
		else:
			return 1 

	i = 1
	while i <= max_digits:
		buckets = defaultdict(list)

		for x in array:
			if digits(x) > max_digits:
				max_digits = digits(x)

			s = str(x)
			d = s[len(s)-i] if len(s) >= i else 0 
			buckets[int(d)].append(x)

		array = concat_buckets(buckets)
		i += 1 

	return array 


def mom_select(array, k):
	print "K", k 
	n = len(array)
	if n <= 1:
		return array

	def split_array(array):
		r = []
		mini = []
		for i,x in enumerate(array):
			if not (i+1)%5:
				r.append(mini)
				mini = []
			mini.append(x)
		
		# take care of overflow
		if not r:
			r.append(mini)
		else: 
			for i, x in enumerate(mini):
				while len(r) < i + 1:
					i -= 1
				r[i].append(x)
		return r 

	mini_lists = split_array(array)
	medians = [sorted(m)[int(math.floor(len(m)/2))] for m in mini_lists]
	pivot = mom_select(medians, len(medians)/2)[0]
	print "pivot", pivot 

	l, e, g = [], [], []
	for x in array:
		if x < pivot:
			l.append(x)
		elif x > pivot:
			g.append(x)
		else:
			e.append(x)

	if len(l) <= k:
		return mom_select(l, k)
	elif len(l) + len(e) <= k:
		return pivot 
	else:
		return mom_select(g, k - (len(l) + len(e)))


def topo_sort(graph):
	# graph represented as an edge list 
	# O(|V| + |E|)  ]

	Q = Queue()
	sort = []
	n = len(graph[0])

	def has_incident_edges(graph, x):
		for e in graph.values():
			if x in e:
				return True
		return False 

	# push verts with no incident edges 
	for v in graph.keys():
		if not has_incident_edges(graph, v):
			Q.enqueue(v)

	while not Q.isEmpty():
		v = Q.dequeue()
		sort.append(v)
		neighbors = graph[v][:]  # must copy list to remove from graph while iterating
		for u in neighbors:
			graph[v].remove(u)
			if not has_incident_edges(graph, u):
				Q.enqueue(u)

	if sort < n:
		raise StandardError("Cannot sort - graph may have a cycle")
	else:
		return sort 



if __name__ == '__main__':
	# unsorted = [17, 3, 5, 12, 2, 0, -1, 14, 14, -20, 8]
	# print selection_sort(unsorted)
	unsorted = [17, 3, 5, 12, 2, 0, -1, 14, 14, -20, 8]
	unsorted_positive = [17, 3, 5, 12, 2, 0 ,14, 14, 20, 8, 72,1]
	print radix_sort(unsorted_positive)
	#print mom_select(unsorted, 7)

	#mock_graph = [[0,0,0], [1,0,0], [0, 1, 0]]
	#mock_graph = {0:[1], 1:[3,4], 2:[], 3:[2], 4:[]}
	#print topo_sort(mock_graph)
