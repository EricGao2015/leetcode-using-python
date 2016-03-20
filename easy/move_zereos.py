class Solution(object):
	def moveZeroes(self, nums):
		count_0 = nums.count(0)
		i = 0 
		while i<len(nums):
			if(nums[i]==0 and count_0>0):
				del nums[i]
				nums.append(0)
				count_0 -= 1
			else:
				i += 1

nums1 = [0, 3, 5, 0, 2, 0, 5, 6, 8]
nums2 = [0,0,1]
s1 = Solution()
s1.moveZeroes(nums1)

s2 = Solution()
s2.moveZeroes(nums2)
