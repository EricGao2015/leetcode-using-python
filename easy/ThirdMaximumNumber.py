class Solution(object):
	def thirdMax(self, nums):
		firstMax = min(nums)
		secondMax = firstMax
		thirdMax = secondMax
		for num in nums:
			if num==firstMax or num==secondMax or num==thirdMax:
				continue
			else:
				if num>firstMax:
					thirdMax = secondMax
					secondMax = firstMax
					firstMax = num
				elif num>secondMax:
					thirdMax = secondMax
					secondMax = num
				elif num>thirdMax:
					thirdMax = num
		if firstMax==secondMax or secondMax==thirdMax or firstMax==thirdMax:
			return firstMax
		else:
			return thirdMax

		"""
		:type nums: List[int]
		:rtype: int
		"""
def main():
	S = Solution()
	nums = [3,1,1,1]
	print S.thirdMax(nums)

if __name__ == '__main__':
	main()
