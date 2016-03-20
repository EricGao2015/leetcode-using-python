class Solution(object):
	def singleNumber(self, nums):
		result = nums[0]
		for i in range(1,len(nums)):
			result ^= nums[i]
		return result

	# def singleNumber(self, nums):   # time exceed error.
	# 	while(1):
	# 		temp = nums[0]
	# 		nums.remove(temp)
	# 		try:
	# 			nums.remove(temp)
	# 		except ValueError:
	# 			return temp


if __name__ == '__main__':
	s = Solution()
	nums = [1,2,3,4,5,9,1,2,3,4,5]
	print s.singleNumber(nums)
    		
