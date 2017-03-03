class Solution(object):
    def convertToBase7(self, num):
        if num is 0:
            return "0"
        if num<0:
            flag = "-"
            num *= -1
        else:
            flag = ""
        result = ""
        while num is not 0:
            result = str(num%7) + result
            num = num - num%7
            num /= 7

        return  flag + result
        """
        :type num: int
        :rtype: str
        """

def main():
    s = Solution()
    for num in range(-20,30):
        print s.convertToBase7(num)
    print s.convertToBase7(-7)

if __name__ == '__main__':
    main()