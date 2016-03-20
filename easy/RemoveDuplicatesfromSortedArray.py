class Solution(object):
	def removeDuplicates(self, nums):
		i,len_s = 0,len(nums)
		while i<len(nums)-1:
			if nums[i]==nums[i+1]:
				del nums[i]
				len_s -= 1
			else:
				i += 1
		return len(nums)


if __name__=='__main__':
	s = Solution()
	nums = [1,1,2,2,2,2,3,3,4,5,6,6,6,7,8]
	print s.removeDuplicates(nums)
	print s.removeDuplicates([1,2])
	print s.removeDuplicates([])
	print s.removeDuplicates([1])