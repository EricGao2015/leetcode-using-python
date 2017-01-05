class Solution(object):
    # def strStr(self, haystack, needle):
    # 	return haystack.find(needle)
    def strStr(self, haystack, needle):
        if len(needle) is 0:
            return 0
        len_main = len(haystack)
        len_sub = len(needle)
        main_index = 0
        next_index = 0
        while main_index<=(len_main-len_sub):
            sub_index = 0
            next_index = main_index + len_sub

            while haystack[main_index] is needle[sub_index]:
                sub_index += 1
                if sub_index is len_sub:
                    return main_index - len_sub + 1
                main_index += 1

            if next_index>=len_main:
                return -1

            last_index = -1;
            for i in range(len_sub-1, -1, -1):
                if needle[i] is haystack[next_index]:
                    last_index = i
                    break
            main_index = next_index - last_index
        return -1
if __name__=="__main__":
    s = Solution()
    haystack = ''
    needle = ''

    main= "This nic is a nice algorithm."
    substring1 = "nic is a nice algorithm."
    substring2 = "This"
    substring3 = "is a"
    substring4 = "ce algo"
    substring5 = "m4m."
    substring6 = "This nic is a nice algorithm."
    substring7 = "Thi s"
    substring8 = "nic"
    substring9 = "algorithm.2"
    substring10 = "This.123"
    substring11 = "This nic is a nice algorithm.123"

    print s.strStr(main, substring1), "  ", main.find(substring1)
    print s.strStr(main, substring2), "  ", main.find(substring2)
    print s.strStr(main, substring3), "  ", main.find(substring3)
    print s.strStr(main, substring4), "  ", main.find(substring4)
    print s.strStr(main, substring5), "  ", main.find(substring5)
    print s.strStr(main, substring6), "  ", main.find(substring6)
    print s.strStr(main, substring7), "  ", main.find(substring7)
    print s.strStr(main, substring8), "  ", main.find(substring8)
    print s.strStr(main, substring9), "  ", main.find(substring9)
    print s.strStr(main, substring10), "  ", main.find(substring10)
    print s.strStr(main, substring11), "  ", main.find(substring11)
    print s.strStr("", "")
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
