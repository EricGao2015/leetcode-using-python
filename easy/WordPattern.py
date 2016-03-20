class Solution(object):
	def wordPattern(self, pattern, str):
		str_list = str.split()
		pattern_l = [pattern[i] for i in range(len(pattern))]
		if(len(str_list)==len(pattern) and len(set(str_list))==len(set(pattern))):
			zip_ps = zip(pattern_l, str_list)
			return len(set(pattern_l))==len(set(zip_ps))	
		else:
			return False

if __name__ == '__main__':
	s = Solution()
	print s.wordPattern('abba','dog dog dog dog')