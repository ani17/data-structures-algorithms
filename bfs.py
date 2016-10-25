class Node:
	"""Node Structure"""
	def __init__(self, arg):
		self.data = arg
		self.left = None
		self.right = None

def bfs(root):
	""" Breadth First Traversal """
	if root is None:
		return

	queue = []

	queue.append(root)

	while (len(queue) > 0):
			print queue[0].data
			node = queue.pop(0)


			if node.left is not None:
				queue.append(node.left)

			if node.right is not None:
				queue.append(node.right)


root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(9)
root.right.left = Node(10)
root.right.right = Node(11)
bfs(root)