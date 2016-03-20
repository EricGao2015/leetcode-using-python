class Solution(object):
    def reverseBits(self, n):
    	re,i = 0,0
    	while n!=0:
    		re = n%2+re*2
    		n /= 2
    		i += 1
    	return re*(2**(32-i))


if __name__=='__main__':
	s = Solution()
	print s.reverseBits(43261596)
	print s.reverseBits(1025)