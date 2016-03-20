# https://leetcode.com/problems/pascals-triangle-ii/
class Solution(object):
	def getRow(self, rowIndex):
		rowIndex += 1
		re = [1]*rowIndex
		factorial = [1]*rowIndex
		for i in range(1,rowIndex):
			factorial[i] = factorial[i-1]*i
		for i in range(1, int((rowIndex+1)/2.0)):
			re[i] = re[rowIndex-1-i] = factorial[rowIndex-1]/(factorial[i]*factorial[rowIndex-1-i])
		return re


if __name__=='__main__':
	s = Solution()
	for i in range(10):
		print s.getRow(i)