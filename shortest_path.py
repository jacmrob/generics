import numpy as np 
from heap import Heap, HeapNode

class GraphNode:
	def __init__(self, data):
		self.data = data 
		self.dist = np.inf 
		self.prev = None 


def make_graph():
	graph = {}
	graph['A'] = {'node': GraphNode('A'), 'edges': [(4, 'B')]}
	graph['B'] = {'node': GraphNode('B'), 'edges': [(3, 'C'), (5, 'D')]}
	graph['C'] = {'node': GraphNode('C'), 'edges': [(1, 'D')]}
	graph['D'] = {'node': GraphNode('D'), 'edges': []}

	return graph 


def dijkstras(graph, s):
	# dict of node_data -> {'node': GraphNode,
	#  						'edges': [(edge weight, node_data it points to)]}

	PQ = Heap() 

	def _heap_nodify(node):
		print "making heap node with priority", node.dist, " and data ", node.data
		return HeapNode(node.dist, node.data) 

	graph[s]['node'].dist = 0 
	for v in graph.values():
		PQ.insert(_heap_nodify(v['node']))

	removed = []

	while not PQ.is_empty():
		u_heap_node = PQ.remove_min()
		u_key = u_heap_node.data 
		if u_key not in removed:
			print u_key 
			removed.append(u_key)
			u = graph[u_key]['node']
			edges = graph[u_key]['edges']
			for edge in edges:
				v = graph[edge[1]]['node']
				print v 
				cost_u_v = edge[0]
				if v.dist > u.dist + cost_u_v:
					v.dist = u.dist + cost_u_v
					v.prev = u 
					PQ.insert(_heap_nodify(v))

if __name__ == '__main__':

	g = make_graph()
	dijkstras(g, 'A')
	print g

