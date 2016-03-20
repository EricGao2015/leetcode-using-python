class Solution(object):
	def generate(self, numRows):
		re = []
		for i in range(0,numRows):
			re.append([1]*(i+1))
			for j in range(1,i):
				re[i][j] = re[i-1][j-1]+re[i-1][j]
		return re

if __name__=='__main__':
	s = Solution()
	print s.generate(6)