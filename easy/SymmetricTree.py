# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSymmetric0(self, root):
		if not root:
			return True
		else:
			stack = [(root.left,root.right)]
			while stack:
				l,r = stack.pop()
				if not l and not r:
					continue
				elif None in (l,r):
					return False
				elif l.val==r.val:
					stack.append((l.left, r.right))
					stack.append((l.right, r.left))
				else:
					return False
			return True

	def isSymmetric1(self, root):
		if not root:
			return False
		else:
			return self.fun1(root.left, root.right)

	def fun1(self, left, right):
		if not left and not right:
			return True
		elif None in (left, right):
			return False
		elif left.val==right.val:
			return self.fun1(left.left, right.right) and self.fun1(left.right, right.left)
		else:
			return False


if __name__=="__main__":
	s = Solution()
	root1 = TreeNode(0)
	root1.left, root1.right = TreeNode(1), TreeNode(2)
	root1.left.left = TreeNode(3)
	root1.left.left.left = TreeNode(4)

	# root2 = TreeNode(0)
	# root2.left, root2.right = TreeNode(1), TreeNode(2)
	# root2.left.left = TreeNode(3)
	# root2.left.left.left = TreeNode(4)

	print s.isSymmetric0(root1)
	"""
	:type root: TreeNode
	:rtype: bool
	"""