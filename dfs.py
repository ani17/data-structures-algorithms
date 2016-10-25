class Node:
	""" Node structure """
	def __init__(self, arg):
		self.data = arg
		self.left = None
		self.right = None

def preorder(root):
	if root is None:
		return
	
	print root.data
	
	if root.left is not None:
		preorder(root.left)
	if root.right is not None:
		preorder(root.right)

def inorder(root):
	if root is None:
		return

	if root.left is not None:
		inorder(root.left)

	print root.data

	if root.right is not None:
		inorder(root.right)

def postorder(root):
	if root is None:
		return
	
	if root.left is not None:
		postorder(root.left)
	if root.right is not None:
		postorder(root.right)

	print root.data


def dfs(root):
	""" Depth First Traversal - Preorder(VLR), Inorder(LVR) & Post Order(LRV) """
	print "Preorder"
	preorder(root)

	print "inorder"
	inorder(root)

	print "postorder"
	postorder(root)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

dfs(root)