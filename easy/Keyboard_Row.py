class Solution(object):
    def findWords(self, words):
        return [word for word in words if self.find(word)]

    def find(self, word):
        s1 = {'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'}
        s2 = {'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'}
        s3 = {'z','x','c','v','b','n','m','Z','X','C','V','B','N','M'}
        if word[0] in s1:
            s = s1
        elif word[0] in s2:
            s = s2
        else:
            s = s3
        for w in word:
            if w not in s:
                return False
        return True


        """
        :type words: List[str]
        :rtype: List[str]
        """

def main():
    s = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print s.findWords(words)

if __name__ == '__main__':
    main()