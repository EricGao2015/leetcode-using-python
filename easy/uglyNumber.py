class Solution(object):
	def isUgly(self, num):
		if(num>0):
			for i in [10,8,6,5,3,2]:
				while num%i==0:
					num = num/i
			return num==1
		else:
			return False

if __name__ == '__main__':
	s = Solution()
	for i in range(100):
		s.isUgly(i)