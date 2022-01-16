class Node:
	def __init__(self,d):
		self.data = d
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def addNode(self, node, d):
		if self.root is None:
			self.root = Node(d)
			return

		# if value is less than the current node
		# move to left subtree
		if d <= node.data:
			if node.left is None:
				node.left = Node(d)
			else:
				node = node.left
				self.addNode(node,d)
		
		# if value is greater than the current node
		# move to right subtree
		else:
			if node.right is None:
				node.right = Node(d)
			else:
				node = node.right
				self.addNode(node,d)

	def insert(self, d):
		self.addNode(self.root, d)

	def insertData(self):
		A = [4, 2, 1, 5, 3, 0]
		for num in A:
			self.insert(num)

	def traverse(self, node):  
		if self.root is None:
			print("Tree is empty")
		else:
			print(node.data)
			if node.left is not None:
				self.traverse(node.left)
			# else:
			# 	print(None)
			if node.right is not None:
				self.traverse(node.right)
			# else:
			# 	print(None)
			# 	
	
	def search(self, node, val):
		if node.data == val:
			print(f"Found val : {val}")
			return
		else:
			if val < node.data:
				if node.left is not None:
					node = node.left
					return self.search(node, val)
			else:
				if node.right is not None:
					node = node.right
					return self.search(node,val)

		print(f"{val} not found")

	def remove(self, val):
		self.delete(self.root,val)

	# Explanation @ mycodeschool : https://www.youtube.com/watch?v=gcULXE7ViZw
	def delete(self, node, val):
		if node is None:
			return None

		if val < node.data:
			node.left = self.delete(node.left, val)
			return node
		elif val > node.data:
			node.right = self.delete(node.right, val)
			return node
		elif val == node.data:
			# case 1 : node has no children
			if node.left is None and node.right is None:
				del node
				return None
			
			# case 2 : node has 1 child
			if node.left is None:
				temp = node
				node = node.right
				del temp
				return node

			if node.right is None:
				temp = node
				node = node.left
				del temp
				return node

			# case 3: node has 2 children 
			if node.left is not None and node.right is not None:
				# Find minimum val from right subtree 
				minNode = self.findMin(node.right)
				# Assign the data of node with min val to current node
				node.data = minNode.data
				# Delete the node with min val
				node.right = self.delete(node.right, minNode.data)
				return node

	def findMin(self, node):
		temp = node
		while temp.left is not None:
			temp = temp.left
		return temp

	def levelOrderTraversal(self):
		Q = []
		Visited = []
		
		if len(Q) == 0:
			Q.append(self.root)
		
		while len(Q) > 0:
			pop = Q[0]
			Visited.append(pop)
			Q = Q[1:]
			
			# Find Neighbours of popped element
			if pop.left is not None:
				Q.append(pop.left)
			if pop.right is not None:
				Q.append(pop.right)
		
		# level order traversal
		T = []
		for node in Visited:
			T.append(node.data)
		print(f"Level Order Traversal: {T}")
			


btree = BST()
btree.insertData()
# btree.traverse(btree.root)
# btree.search(btree.root,10)
# btree.root = btree.delete(btree.root,1)
print("Before")
btree.levelOrderTraversal()
btree.remove(0)
print("After Removal")
btree.levelOrderTraversal()
