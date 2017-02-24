class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count, count = 0, 0
        last_is_1 = False
        for num in nums:
            if num is 1:
                if last_is_1:
                    count += 1
                else:
                    count = 1
                    last_is_1 = True
            else:
                last_is_1 = False
            max_count = max(max_count, count)
        return max_count
        """
        :type nums: List[int]
        :rtype: int
        """

if __name__ == '__main__':
    s = Solution()
    # nums = [1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1]
    nums = [0,1]
    print s.findMaxConsecutiveOnes(nums)
