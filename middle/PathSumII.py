# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def pathSum0(self, root, sum):
		if root:
			stack = [[root, [root.val], root.val]]
			result = []
			while stack:
				current, val_list, sum_val = stack.pop()
				if not current.left and not current.right and sum_val == sum:
					result.append(val_list)
				if current.left:
					val_list.append(current.left.val)
					stack.append([current.left, val_list[:], current.left.val+sum_val])
				if current.right:
					if current.left:
						val_list.pop()
					val_list.append(current.right.val)
					stack.append([current.right, val_list[:], current.right.val+sum_val])
			return result
		else:
			return []


	def pathSum1(self, root, sum):
		if root:
			stack = [[root, [root.val], root.val]]
			result = []
			while stack:
				current, val_list, sum_val = stack.pop()
				if not current.left and not current.right and sum_val == sum:
					result.append(val_list)
				if current.left:
					stack.append([current.left, val_list+[current.left.val], current.left.val+sum_val])
				if current.right:
					stack.append([current.right, val_list+[current.right.val], current.right.val+sum_val])
			return result
		else:
			return []

if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.right.right = TreeNode(6)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(4)
	print s.pathSum1(root, 8)
	"""
	:type root: TreeNode
	:type sum: int
	:rtype: List[List[int]]
	"""
	    