# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def minDepth0(self, root):     #BSF
		if root:
			bsf_list = [(root, 1)]
			while bsf_list:
				for i in range(len(bsf_list)):
					current, depth = bsf_list.pop(0)
					if (None,None) == (current.left,current.right):
						return depth
					if current.left:
						bsf_list.append((current.left, depth+1))
					if current.right:
						bsf_list.append((current.right, depth+1))
		else:
			return 0

	def minDepth1(self, root):
		if not root:
			return 0
		if not root.left or not root.right:
			return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
		else:
			return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__=="__main__":
	s = Solution()
	root = TreeNode(0)
	root.left, root.right = TreeNode(1), TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(4)
	print s.minDepth0(root)
        """
        :type root: TreeNode
        :rtype: int
        """
        