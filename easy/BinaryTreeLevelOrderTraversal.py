# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrder(self, root):
		if root:
			bsf_list = [(root,root.val)]
			result = []
			while bsf_list:
				result.append([i[1] for i in bsf_list])
				for i in range(len(bsf_list)):
					current,sth = bsf_list.pop(0)
					if current.left:
						bsf_list.append((current.left, current.left.val))
					if current.right:
						bsf_list.append((current.right, current.right.val))
			return result
		else:
			return []

if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(4)
	root.right.right = TreeNode(5)
	root.right.right.right = TreeNode(6)
	print s.levelOrder(root)
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
        