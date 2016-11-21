class Solution(object):
	def findKthLargest(self, nums, k):
		for i in xrange(k):
			for j in xrange(i+1, len(nums)):
				if nums[i]<nums[j]:
					nums[i], nums[j] = nums[j], nums[i]
		return nums[k-1]

	def findKthLargest1(self, nums, k):
		for i in xrange(k):
			nums[0] = nums[i]
			for j in xrange(i+1, len(nums)):
				if nums[0]<nums[j]:
					temp = nums[0]
					nums[0] = nums[j]
					nums[j] = temp
		return nums[0]

		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
def main():
	S = Solution()
	nums = [1]
	k = 1
	print S.findKthLargest(nums, k)

if __name__ == '__main__':
	main()
