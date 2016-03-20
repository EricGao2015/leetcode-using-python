class Solution(object):
	def searchInsert0(self, nums, target):
		for i in range(len(nums)):
			if nums[i]>=target:
				return i
		return i+1


if __name__=="__main__":
	s = Solution()
	nums = [1,3,5,6]
	target = 8
	print s.searchInsert(nums, target)
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""