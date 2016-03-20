# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	# def maxDepth(self, root):          #too slow.
	# 	if root:
	# 		l = self.maxDepth(root.left)
	# 		r = self.maxDepth(root.right)
	# 		return max(l,r)+1
	# 	else:
	# 		return 0

if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(4)
	print s.maxDepth(root)
	"""
	:type root: TreeNode
	:rtype: int
	"""