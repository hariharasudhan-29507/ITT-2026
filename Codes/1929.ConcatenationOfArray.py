class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=[]
        for i in range (len(nums)):
            nums1.append(nums[i])
        for i in nums1:
            nums.append(i)
        return nums
s=Solution()
print(s.getConcatenation([1,2,1]))