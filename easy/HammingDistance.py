class Solution(object):
    def hammingDistance(self, x, y):
        a = x^y
        res = 0
        while a>0:
            res += a&1
            a >>= 1
        return res;

        """
        :type x: int
        :type y: int
        :rtype: int
        """

def main():
    s= Solution()
    for i in range(20):
        for j in range(20):
            print i, j, s.hammingDistance(i,j)

if __name__ == '__main__':
    main()
