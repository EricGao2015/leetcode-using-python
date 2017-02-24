class Solution(object):
    def findComplement0(self, num):
        s = bin(num).replace('0b','').replace('1', '*').replace('0', '1').replace('*','0')
        return int(s, 2)
        """
        :type num: int
        :rtype: int
        """

    def findComplement(self, num):
        stack = []
        res = 0
        i = 0
        while num:
            res += 2**i * (1-num&1)
            i += 1
            num >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    num = 13213245
    print s.findComplement(num), s.findComplement0(num)
