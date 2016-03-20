# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree1(self, p, q):
		if p and q:
			l = self.isSameTree(p.left, q.left)
			r = self.isSameTree(p.right, q.right)
			return l and r and p.val==q.val
		else:
			return p == q
			
	def isSameTree2(self, p, q):
	    stack = [(p, q)]
	    while stack:
	        node1, node2 = stack.pop()
	        if not node1 and not node2:
	            continue
	        elif None in [node1, node2]:
	            return False
	        else:
	            if node1.val != node2.val:
	                return False
	            stack.append((node1.right, node2.right))
	            stack.append((node1.left, node2.left))
	    return True

if __name__=="__main__":
	s = Solution()
	root1 = TreeNode(0)
	root1.left, root1.right = TreeNode(1), TreeNode(2)
	root1.left.left = TreeNode(3)
	root1.left.left.left = TreeNode(4)

	root2 = TreeNode(0)
	root2.left, root2.right = TreeNode(1), TreeNode(2)
	root2.left.left = TreeNode(3)
	root2.left.left.left = TreeNode(4)
	print s.isSameTree(root1, root2)
	"""
	:type p: TreeNode
	:type q: TreeNode
	:rtype: bool
	"""