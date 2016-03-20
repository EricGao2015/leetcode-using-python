class Solution(object):
	def missingNumber0(self, nums):
		a = 0
		b = 0
		for i in nums:
			b ^=  a^i
			a += 1 
		return a^b 

	def missingNumber1(self, nums):
		length = len(nums)
		return length*(length+1)/2-sum(nums)


if __name__=="__main__":
	s = Solution()
	nums = [0,1,2,3,4,5,6,7,8]
	# nums = [1,0]
	print s.missingNumber1(nums)
	"""
	:type nums: List[int]
	:rtype: int
	"""