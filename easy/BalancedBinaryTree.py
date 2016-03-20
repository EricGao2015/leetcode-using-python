# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isBalanced(self, root):
		if not root:
			return True
		else:
			return self.depth(root)!=-1
	def depth(self, root):
		if not root:
			return 0
		else:
			l,r = self.depth(root.left),self.depth(root.right)
			if abs(l-r)>1 or l==-1 or r==-1:
				return -1
			return max(l,r)+1

if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(6)
	root.left.left.left = TreeNode(4)
	root.right.right = TreeNode(5)
	print s.isBalanced(root)
	"""
	:type root: TreeNode
	:rtype: bool
	"""
        