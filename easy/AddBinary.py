class Solution(object):
	def addBinary(self, a, b):
		if len(a)<len(b):
			a,b = b,a
		b = "0"*(len(a)-len(b))+b
		result = ""
		flag = 0
		for i in range(1,len(a)+1):
			t = int(a[-i]) + int(b[-i]) + flag
			result += str(t%2)
			flag = 1 if t>1 else 0
		if flag==1:
			result += "1"
		return result[::-1]


if __name__=="__main__":
	s = Solution()
	a = "1111"
	b =  "1111"
	print s.addBinary(a, b)
        """
        :type a: str
        :type b: str
        :rtype: str
        """