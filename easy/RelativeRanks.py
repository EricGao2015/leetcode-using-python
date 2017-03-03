class Solution(object):
    def findRelativeRanks(self, nums):
        index_scr_dic = {}
        for i, num in enumerate(nums):
            index_scr_dic[i] = num
        nums.sort(reverse=True)
        src_rank_dic = {}
        for i,num in enumerate(nums):
            src_rank_dic[num] = i
        return [self.GetRank(src_rank_dic[index_scr_dic[n]]) for n in range(len(nums))]
        """
        :type nums: List[int]
        :rtype: List[str]
        """
    def GetRank(self, val):
        if val is 0:
            return "Gold Medal"
        elif val is 1:
            return "Silver Medal"
        elif val is 2:
            return "Bronze Medal"
        else:
            return str(val+1)
def main():
    s = Solution()
    nums = [10,3,8,9,4]
    print s.findRelativeRanks(nums)

if __name__ == '__main__':
    main()