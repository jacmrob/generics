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
		parent = i / 2 if self.is_even(i) else (i - 1) / 2
		while i > 1 and self.elements[i].priority < self.elements[parent].priority:
			self.fast_swap(self.elements, i, parent)
			i = parent
			parent = i / 2 if self.is_even(i) else (i - 1) / 2 

	def downheap(self):
		i = 1 
		while (i < self.length - 2) and ((self.elements[i].priority < self.elements[i + 1].priority) or (self.elements[i].priority < self.elements[i + 2].priority)):
			swap_i = i + 1 if self.elements[i + 1].priority < self.elements[i + 2].priority else i + 2
			self.fast_swap(self.elements, i, swap_i)
			i = swap_i

	def insert(self, priority, data):
		n = HeapNode(priority, data)
		self.elements.append(n)
		self.length += 1 
		self.complete = not self.complete  # flip sign
		self.upheap(self.length)

	def remove_min(self):
		self.fast_swap(self.elements, 1, self.length)  # swap first and last thing
		m = self.elements.pop()
		self.downheap()
		self.length -= 1 
		return m 

	def peek_min(self):
		pass

	def fast_swap(self, array, i1, i2):
		array[i1], array[i2] = array[i2], array[i1]

	def is_even(self, n):
		return n % 2 < 1 


def build_heap_from_map(input_map):
	heap = Heap()
	for k,v in input_map.iteritems():
		heap.insert(k, v)

	return heap 


# TODO: write heap unit tests 

if __name__ == '__main__':
	m = {1:'jackie', 2: 'gina', 17:'alex', 6:'aaron', 27:'dana'}
	heap = build_heap_from_map(m)
	while not heap.is_empty():
		x = heap.remove_min()
		print x.data 

