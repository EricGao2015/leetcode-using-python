# https://leetcode.com/problems/palindrome-number/
class Solution(object):
	def isPalindrome(self, x):
		str_x = str(x)
		return str_x == str_x[::-1]

if __name__=='__main__':
	s = Solution()
	print s.isPalindrome(-123)
	print s.isPalindrome(123321)
	print s.isPalindrome(123456)
	print s.isPalindrome(1230)
	print s.isPalindrome(120003)