import math,time
# class Solution(object):
# 	def isPowerOfThree(self, n):
# 		return n > 0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10
# 0.142999887466

class Solution(object):
	def isPowerOfThree(self, n):
		if(n>0):
			while(n!=0):
				if(n%3!=0 and n!=1):
					return False
				else:
					n = n/3
			if(True):
				return True
		else:
			return False
# 0.177999973297,0.055999994278

start = time.time()
for i in range(100):
	s1 = Solution()
	print i,s1.isPowerOfThree(i)
end = time.time()
print end-start
