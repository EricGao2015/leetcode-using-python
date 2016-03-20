class Solution(object):
	def merge(self, nums1, m, nums2, n):
		i,j = 0,0
		while(j<n and m+j>i):
			if(nums1[i]>=nums2[j]):
				nums1.insert(i,nums2[j])
				i += 1
				j += 1
			else:
				i += 1
		while j<n:
			nums1.append(nums2[j])
			j += 1 
		return nums1

if  __name__ == '__main__':
	s = Solution()
	nums1 = [0,5]
	nums2 = [1]               # 5,7,8,9,20,22,23,89
	m,n = len(nums1),len(nums2)
	print s.merge(nums1, m, nums2, n)