class Solution(object):
	def convert(self, s, numRows):
		if numRows==1:
			return s
		else:
			l = [""]*numRows
			for i in range(len(s)):
				index = i%(2*numRows-2) 
				if index>numRows-1:
					index = 2*numRows-2-index
				l[index] += s[i]
			return "".join(l)

if __name__=="__main__":
	S = Solution()
	s = "PAYPALISHIRING"
	s = "gaoqihang"
	numRows = 3
	print S.convert(s, numRows)
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        