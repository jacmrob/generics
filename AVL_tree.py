

# balance factor of node: left subtree height - right subtree height

class Node:
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None


class AVL_tree:

	def __init__(self):
		self.height = -1  # empty tree 
		self.balance = 0 
		self.node = None

	def insert(self, data):
		n = Node(data)

		# if tree is empty insert at root
		if self.node == None:
			self.node = n 
			self.node.left = AVL_tree()
			self.node.right = AVL_tree()

		# if data is less than root, insert into left subtree
		elif data < self.node.data:
			self.node.left.insert(data)

		# if data is greater than root, insert into right subtree 
		elif data > self.node.data:
			self.node.right.insert(data)

		self.height = max(self.node.left.height + self.node.right.height) + 1 
		self.balance = self.node.left.height - self.node.right.height 

		self.rebalance()

	def rebalance(self):
		#self.update_balances()
		#self.update_heights()

		while self.balance < -1 or self.balance > 1:
			if self.balance > 1:
				if self.node.left.balance < 0 

	def update_balances(self):
		if self.node:
			if self.node.left:
				self.node.left.update_balances()
			if self.node.right:
				self.node.right.update_balances() 
			self.balance = self.node.left.height - self.node.right.height
		else:
			self.balance = 0 

	def update_heights(self):
		if self.node:
			if self.node.left:
				self.node.left.update_heights()
			if self.node.right:
				self.node.right.update_heights()
			self.height = 1 + max(self.node.left.height, self.node.right.height)
		else:
			self.height = -1 



		# require single rotation
		# case 1: insert into left subtree of left child
		# case 2: insert into right subtree of right child 

		# require double rotation
		# case 3: insert into right subtree of left child
		# case 4: insert into left subtree of right child 

