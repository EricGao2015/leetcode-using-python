class Solution(object):
	def isPalindrome0(self, s):       #too slow.
		if not s:
			return True
		else:
			l = ''
			s = s.upper()
			for i in s:
				if ord(i) in range(48, 58) + range(65, 91):
					l += i
			for i in range(len(l)/2):
				if l[i] != l[-i-1]:
					return False
			return True

	def isPalindrome1(self, s):       #too slow.
		if not s:
			return True
		else:
			l = ''
			for i in s:
				if ord(i) in range(48, 58) + range(97, 123):
					l += i
				elif ord(i) in range(65, 91):
					l += chr(ord(i)+32)
			for i in range(len(l)/2):
				if l[i] != l[-i-1]:
					return False
			return True

		def isPalindrome2(self, s):
			if not s:
				return True
			else:
				




if __name__=="__main__":
	S = Solution()
	s = "A man, a plan, a canal: Panama"
	# print s.lower().strip()
	print S.isPalindrome1(s)
	"""
	:type s: str
	:rtype: bool
	"""