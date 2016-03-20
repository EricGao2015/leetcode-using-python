class Solution(object):
	def canWinNim(self, n):
		if(n%4==0):
			return False
		else:
			return True

for i in range(50):
	S1 = Solution()
	print S1.canWinNim(i)