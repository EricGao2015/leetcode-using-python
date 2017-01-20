# 34. Search for a Range
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        head, tail = 0, len(nums)-1
        foundhead, foundtail = False, False
        while head is not tail:
            if not foundhead:
                if nums[head] is target:
                    foundhead = True
                else:
                    head += 1

            if not foundtail:
                if nums[tail] is target:
                    foundtail = True
                else:
                    tail -= 1

            if foundhead and foundtail:
                break
            if head > tail:
                head, tail = -1, -1
                break
        if nums[head] is not target:
            return [-1, -1]
        else:
            return [head, tail]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 81
    nums = [1, 1, 7, 8]
    nums = []
    target = 7
    s = Solution()
    print s.searchRange(nums, target)

if __name__ == '__main__':
    main()
