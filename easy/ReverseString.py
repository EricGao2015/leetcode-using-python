class Solution(object):
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if len(s)<2:
			return s
		else:
			s = list(s)
			l = len(s)
			for i in range(l/2):
				s[i], s[-(i+1)] = s[-(i+1)], s[i]
			return "".join(s)

if __name__ == '__main__':
	s = Solution()
	str = "gao"
	print s.reverseString(str)