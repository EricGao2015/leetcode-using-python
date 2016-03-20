# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		if head.next:
			Node1, Node2 = head, head
			for i in range(n):
				Node2 = Node2.next
			if not Node2:
				return head.next
			while Node2.next:
				Node2 =  Node2.next
				Node1 = Node1.next
			Node1.next = Node1.next.next
			return head
		else:
			return None

if __name__=="__main__":
	s = Solution()
	head = ListNode(1)
	node = head
	for i in range(2, 6):
		node.next = ListNode(i)
		node = node.next
	n = 5
	b = s.removeNthFromEnd(head, n)
	while b:
		print b.val
		b = b.next
	"""
	:type head: ListNode
	:type n: int
	:rtype: ListNode
	"""