class Solution(object):
	def hammingWeight(self, n):
		counts = 0
		while(n!=0):
			if(n%2==1):
				counts += 1
			n /= 2
		return counts


if __name__=='__main__':
	s = Solution()
	print s.hammingWeight(11)