import numpy as np 
from heap import Heap, HeapNode


class GraphNode:
	def __init__(self, data):
		self.data = data 
		self.dist = np.inf 
		self.prev = None 


def make_graph():
	# makes a mock graph to use for testing shortest path algs 
	# dict of node_data -> {'node': GraphNode,
	#  						'edges': [(edge weight, node_data it points to)]}
	graph = {}
	graph['A'] = {'node': GraphNode('A'), 'edges': [(4, 'B')]}
	graph['B'] = {'node': GraphNode('B'), 'edges': [(3, 'C'), (5, 'D')]}
	graph['C'] = {'node': GraphNode('C'), 'edges': [(1, 'D')]}
	graph['D'] = {'node': GraphNode('D'), 'edges': []}

	return graph 


def dijkstras(graph, s):
	# average O(|E| * log|V|)
	# worst O(|V|^2)

	PQ = Heap() 
	def _heap_nodify(node):
		return HeapNode(node.dist, node.data) 

	graph[s]['node'].dist = 0 
	for v in graph.values():
		PQ.insert(_heap_nodify(v['node']))

	removed = []

	while not PQ.is_empty():
		u_heap_node = PQ.remove_min()
		u_key = u_heap_node.data 

		if u_key not in removed:
			removed.append(u_key)
			u = graph[u_key]['node']
			edges = graph[u_key]['edges']

			for edge in edges:
				v = graph[edge[1]]['node']
				cost_u_v = edge[0]
				if v.dist > u.dist + cost_u_v:
					v.dist = u.dist + cost_u_v
					v.prev = u_key 
					PQ.insert(_heap_nodify(v))


def get_path(graph, n):
	# note: this must be traversed backwards to get from target node to start node
	path = []
	while graph[n]['node'].prev:
		n = graph[n]['node'].prev 
		path.append(n) 
	return path 


if __name__ == '__main__':

	g = make_graph()
	dijkstras(g, 'A')
	
	print get_path(g, 'D') 

