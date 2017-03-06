class Solution(object):
    def nextGreaterElement0(self, findNums, nums):
        result = []
        length_nums = len(nums)
        for n in findNums:
            start = nums.index(n)
            flag = False
            for i in range(start+1, length_nums):
                if nums[i]>n:
                    result.append(nums[i])
                    flag = True
                    break
            if not flag:
                result.append(-1)
        return result

    def nextGreaterElement(self, findNums, nums):
        result = []
        for i,num in enumerate(nums):
            for fn in findNums:
                if num is fn:
                    print "i = ", i, fn
                    flag = False
                    for k in range(i+1, len(nums)):
                        if nums[k]>num:
                            result.append(nums[k])
                            flag = True
                            break
                    if not flag:
                        result.append(-1)
        return result

        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

def main():
    s = Solution()
    findNums = [4, 1, 2]
    nums = [1, 3, 4, 2]
    print s.nextGreaterElement(findNums, nums)

if __name__ == '__main__':
    main()