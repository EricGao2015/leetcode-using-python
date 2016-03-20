class Solution(object):
	def summaryRanges(self, nums):
		result = []
		if nums==[]:
			return result
		else:
			start, end = nums[0], nums[0]
			for i in nums[1:]:
				if i==end+1:
					end = i
				else:
					result.append(self.print_start_end(start, end))
					start,end = i,i
			result.append(self.print_start_end(start, end))
			return result
	def print_start_end(self, start, end):
		if start==end:
			return str(start)
		else:
			return str(start)+"->"+str(end)


if __name__=="__main__":
	s = Solution()
	nums = [0,1,2,4,5,7,8,9,10,11,12,19,20,21,36,37,38]
	nums = [12] 
	print s.summaryRanges(nums)
        """
        :type nums: List[int]
        :rtype: List[str]
        """