# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList0(self, head):
		node = head
		l = []
		while node:
			l.append(node.val)
			node = node.next
		node = head
		for i in l[::-1]:
			node.val = i
			node = node.next
		return head

	def reverseList1(self, head):
		forward = None
		while head:
			current = head
			head = head.next
			current.next = forward
			forward = current
		return forward

	def reverseList2(self, head):
		next = None
		while head:
			head.next,head,next =  next,head.next,head

if __name__=="__main__":
	s = Solution()
	head = ListNode(0)
	node = head
	for i in range(1,10):
		node.next = ListNode(i)
		node = node.next
	a = s.reverseList1(head)
	print a.next.val
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
        