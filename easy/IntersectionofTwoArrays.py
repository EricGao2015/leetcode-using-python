class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		res = []
		if len(nums1)<len(nums2):
			nums1, nums2 = nums2, nums1
		for i in nums2:
			if i in nums1 and i not in res:
				res.append(i)
		return res

if __name__ == '__main__':
	s = Solution()
	num1 = [1,1,2,2,3,3,3,8,9,9,6,6]
	num2 = [1,3,5,4,8,96,5,4]
	print s.intersection(num1, num2)
