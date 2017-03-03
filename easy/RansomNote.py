class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for x in set(ransomNote):
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

def main():
    s = Solution()
    ransomNote, magazine = "adf", "b"
    print s.canConstruct(ransomNote, magazine)

if __name__ == '__main__':
    main()