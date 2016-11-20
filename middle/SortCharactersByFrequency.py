class Solution(object):
	def frequencySort(self, s):
		if len(s) is 0:
			return s
		else:
			dic = {}
			for i in s:
				if i not in dic:
					dic[i] = 1
				else:
					dic[i] = dic[i] + 1
			s = ''
			max_val = max(dic.values())
			while max_val is not 0:
				for k,v in dic.items():
					if v is max_val:
						s = s + k*v
						dic[k] = 0
				max_val = max(dic.values())
			return s


		"""
		:type s: str
		:rtype: str
		"""

def main():
	S = Solution()
	S.frequencySort('')

if __name__ == '__main__':
	main()
