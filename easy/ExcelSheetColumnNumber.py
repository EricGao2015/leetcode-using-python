class Solution(object):
	def titleToNumber(self, s):
		Sum = 0
		len_s = len(s)
		for i in range(len_s):
			Sum = ord(s[i])-64 + Sum*26
		return Sum

if __name__=='__main__':
	s = Solution()
	print s.titleToNumber('AAA')