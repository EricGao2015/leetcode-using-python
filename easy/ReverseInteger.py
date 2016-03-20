class Solution0(object):
	def reverse(self, x):
		str_x = str(x)
		if x<0:
			result = int(str_x[-1:0:-1])*-1
		else: 
			result = int(str_x[::-1])
		return result*(result<2147483648 and result>=-2147483648)


class Solution1(object):
	def reverse(self, x):
		result,flag = 0,1
		if x<-1:
			x *= -1
			flag = -1
		while x!=0:
			result = x%10+result*10
			x /= 10
		return result*flag*(result<2147483648 and result>=-2147483648)


if __name__=='__main__':
	s = Solution()
	print s.reverse(23649)