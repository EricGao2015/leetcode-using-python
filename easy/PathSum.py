# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def hasPathSum0(self, root, sum_):
		stack = [root]
		Poped_list = []
		if root:
			while stack:
				temp = stack[-1]
				l, r = temp.left, temp.right
				if l and l not in Poped_list:
					stack.append(l)
				elif r and r not in Poped_list:
					stack.append(r)
				elif (None,None)==(l,r):
					if sum_ == sum([node.val for node in stack]):
						return True
					Poped_list.append(stack.pop())
				else:
					Poped_list.append(stack.pop())
		return False


	def hasPathSum1(self, root, sum_):
		if root:
			stack = [(root, root.val)]
			while stack:
				temp,temp_val = stack.pop()
				l, r = temp.left, temp.right
				if (None,None)==(l,r):
					if sum_ == temp_val:
						return True
				else:
					if l:
						stack.append((l,l.val+temp_val))
					if r:
						stack.append((r, r.val+temp_val))
		return False

if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(6)
	root.left.left.left = TreeNode(4)
	root.right.right = TreeNode(5)
	sum_ = 456
	print s.hasPathSum1(root, sum_)
	"""
	:type root: TreeNode
	:type sum: int
	:rtype: bool
	"""