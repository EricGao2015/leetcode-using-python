class Solution(object):
	def removeElement(self, nums, val):
		count_n = nums.count(val)
		for i in range(count_n):
			nums.remove(val)
		return nums



s = Solution()
print s.removeElement([5,9],5)
