# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates0(self, head):
		if head:
			current = head
			while current.next:
				if current.next.val == current.val:
					current.next = current.next.next
				else:
					current = current.next
			return head
		else:
			return None

	def deleteDuplicates1(self, head):
		if head:
			current = head
			forward = head
			while current:
				while current.next and current.next.val == current.val:
					current.next = current.next.next
				current = current.next
			return head
		else:
			return None

if __name__=="__main__":
	s = Solution()
	head = ListNode(0)
	node = head
	for i in range(1,5):
		node.next = ListNode(i)
		node = node.next
		node.next = ListNode(i)
		node = node.next
	print s.deleteDuplicates1(head)
	"""
	:type head: ListNode
	:rtype: ListNode
	"""