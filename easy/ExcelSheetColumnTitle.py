class Solution(object):
	def convertToTitle(self, n):
		result = ''
		while n!=0:
			if n%26==0:
				result += 'Z'
				n = (n-1)/26
			else:
				result += chr(n%26+64)
				n = n/26
		return result[::-1]

if __name__=='__main__':
	s = Solution()
	for i in range(1,60):
		print i,s.convertToTitle(i)