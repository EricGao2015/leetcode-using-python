# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def oddEvenList(self, head):
		node1 = head
		odd = head    # jishu.
		even = head.next   # oushu.
		while node1:

		return head

if  __name__=="__main__":
	s = Solution()
	head = ListNode(1)
	node = head
	for i in range(2,11):
		node.next = ListNode(i)
		node = node.next
	print s.oddEvenList(head)
	"""
	:type head: ListNode
	:rtype: ListNode
	"""