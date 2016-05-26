class Solution(object):
	def reverseVowels(self, s):
		vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
		i, j = -1 , len(s)
		if len(s)<2:
			return s
		else:
			s = list(s)
			while 1:
				i += 1
				j -= 1
				while i<j and s[i] not in vowels:
					i += 1
				while i<j and s[j] not in vowels:
					j -= 1
				if s[i] in vowels and s[j] in vowels and i<j:
					s[i], s[j] = s[j], s[i]
				else:
					return "".join(s)
if __name__ == '__main__':
	s = "leetcode"
	s = "aeiou"
	S = Solution()
	print S.reverseVowels(s)