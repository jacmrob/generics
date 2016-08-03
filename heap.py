# author: Jacqueline Roberti

class HeapNode:
	def __init__(self, priority, data):
		self.priority = priority
		self.data = data

class Heap:
	def __init__(self):
		self.elements = [None]
		self.length = 0
		self.complete = False 

	def is_empty(self):
		return self.length == 0 

	def upheap(self, i):
		parent_i = i - 2 if self.complete else i - 1 
		while i > 1 and self.elements[i].priority < self.elements[parent_i].priority:
			self.fast_swap(self.elements, i, parent_i)
			i = parent_i 
			parent_i = i - 2


	def downheap(self):
		i = 1 
		while (i < self.length - 2) and ((self.elements[i].priority < self.elements[i + 1].priority) or (self.elements[i].priority < self.elements[i + 2].priority)):
			swap_i = i + 1 if self.elements[i + 1].priority < self.elements[i + 2].priority else i + 2
			self.fast_swap(self.elements, i, swap_i)
			i = swap_i


	def insert(self, node):
		self.elements.append(node)
		self.length += 1 
		self.complete = not self.complete  # flip sign
		self.upheap(self.length)


	def remove_min(self):
		self.fast_swap(self.elements, 1, self.length)  # swap first and last thing
		m = self.elements.pop()
		self.downheap()
		return m 

	def replace_key(self, k, k2):
		pass 
		# TODO

	def fast_swap(self, array, i1, i2):
		array[i1], array[i2] = array[i2], array[i1]


def build_heap_from_map(map):
	pass 
	# TODO 


if __name__ == '__main__':
	data = [HeapNode(1, 'jackie'), HeapNode(22, 'brad'), HeapNode(13, 'aaron'), HeapNode(4, 'dana'), HeapNode(7, 'mike')]
	heap = Heap() 
	for d in data:
		heap.insert(d)
	
	for e in heap.elements:
		if e is not None:
			print e.priority

	heap.remove_min()

	for e in heap.elements:
		if e is not None:
			print e.priority

