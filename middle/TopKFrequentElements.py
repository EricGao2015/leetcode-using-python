class Solution(object):
	def topKFrequent(self, nums, k):
		dic = {}
		for num in nums:
			if num in dic:
				dic[num] = dic[num] + 1
			else:
				dic[num] = 1
		l = []
		max_val = max(dic.values())
		while k is not 0 and max_val is not 0:
			first_meet = True
			for key,val in dic.items():
				if val is max_val:
					l.append(key)
					k = k - 1
					dic[key] = 0
			max_val = max(dic.values())
		return l

		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

def main():
	S = Solution()
	nums = [1,2,1,2]
	k = 2
	print S.topKFrequent(nums, k)

if __name__ == '__main__':
	main()
