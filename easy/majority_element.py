class Solution(object):
	def majorityElement(self, nums):
		nums_l = list(set(nums))
		for i in nums_l:
			if nums.count(i)>int(len(nums)/2):
				# break
				return i


s = Solution()
nums = [3,2,3]
print s.majorityElement(nums)