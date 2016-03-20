# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def binaryTreePaths(self, root):
		if root:
			stack = [(root, str(root.val))]
			path = []
			while stack:
				current,val = stack.pop()
				if (None,None) == (current.left,current.right):
					path.append(val)
				if current.right:
					stack.append((current.right, val+"->"+str(current.right.val)))
				if current.left:
					stack.append((current.left, val+"->"+str(current.left.val)))
			return path
		else:
			return []


if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(4)
	print s.binaryTreePaths(root)
	"""
	:type root: TreeNode
	:rtype: List[str]
	"""