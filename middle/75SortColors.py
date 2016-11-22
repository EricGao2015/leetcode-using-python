class Solution(object):
	def sortColors(self, nums):
		current = 0
		start = 0
		end = len(nums) - 1
		while current<=end:
			if nums[current] is 0:
				if current is start:
					start = start + 1
					current = current + 1
				else:
					nums[start], nums[current] = nums[current], nums[start]
					start = start + 1
			elif nums[current] is 2:
				nums[end], nums[current] = nums[current], nums[end]
				end = end - 1
			else:
				current = current + 1
			print nums, start, current, end
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

def main():
	S = Solution()
	nums = [1, 0]
	S.sortColors(nums)

if __name__ == '__main__':
	main()
