class Solution(object):
	def twoSum0(self, nums, target):
		for i in range(len(nums)):
			try:
				Index = nums.index(target-nums[i])
			except ValueError:
				continue
			else:
				if Index!=i:
					return [i,Index]

	def twoSum1(self, nums, target):
		for i in range(len(nums)):
			if target-nums[i] in nums and nums.index(target-nums[i])!=i:
				return [i, nums.index(target-nums[i])]

	def twoSum2(self, nums, target):       # hash
		dic = {}
		for i in range(len(nums)):
			if target-nums[i] in dic:
				return [dic[target-nums[i]], i]
			else:
				dic[nums[i]] = i

if __name__=="__main__":
	s = Solution()
	nums = [2, 7, 11, 15]
	# nums = [3, 2, 4]
	target = 26
	print s.twoSum2(nums, target)
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""