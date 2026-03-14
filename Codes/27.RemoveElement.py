class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
         if x != val:
                nums[i] = x
                i += 1
        return i
s=Solution()
s.removeElement([3,2,2,3],3)