class Solution(object):
	def plusOne(self, digits):
		length = len(digits)
		for i in range(length):
			if(digits[length-i-1]==9):
				digits[length-i-1] = 0
			else:
				digits[length-i-1] += 1
				return digits
		digits.insert(0,1)
		return digits

if __name__ == '__main__':
	s = Solution()
	print s.plusOne([1,9])
	print s.plusOne([1,2,9])
	print s.plusOne([1,4,0])
	print s.plusOne([9,9,9])
	print s.plusOne([6,9,8,3,6,9])
