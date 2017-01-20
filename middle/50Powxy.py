class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        elif n==1:
            return x
        else:
            return x * self.myPow(x, n-1)
        """
        :type x: float
        :type n: int
        :rtype: float
        """

def main():
    s = Solution()
    print s.myPow(2,5)
    print s.myPow(1,0)

if __name__ == '__main__':
    main()
