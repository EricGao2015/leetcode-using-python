class Solution(object):
	def productExceptSelf0(self, nums):
		result = [1]*len(nums)
		a = 1
		for i in range(len(nums)):
			result[i] = a
			a *= nums[i]
		a = 1
		for i in range(len(nums)-1,-1,-1):
			result[i] *= a
			a *= nums[i]
		return result
		
if __name__=='__main__':
	s = Solution()
	nums = range(1,10)
	print s.productExceptSelf(nums)
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""