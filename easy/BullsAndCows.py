class Solution(object):
	def getHint(self, secret, guess):
		secret_l,guess_l = [0]*10,[0]*10
		a,b = 0,0
		len_s = len(secret)
		for i in range(len_s):
			secret_l[int(secret[i])] += 1
			guess_l[int(guess[i])] += 1
			if(secret[i]==guess[i]):
				a += 1
		for i in range(10):
			b += min(secret_l[i],guess_l[i])
		return str(a)+'A'+str(b-a)+'B'

if __name__ == '__main__':
	s = Solution()
	print s.getHint('1807', '7810')
	s1 = Solution()
	print s1.getHint('1123', '0111')
	s1 = Solution()
	print s1.getHint('1', '0')
	s1 = Solution()
	print s1.getHint('11324562', '01456262')
	s1 = Solution()
	print s1.getHint('11', '10')
	s1 = Solution()
	print s1.getHint('1122', '2211')
