# Author - Hariharasudhan A
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums: # traverse with every element
         if x != val: # match element with target value
                nums[i] = x # only keep the elements that are not target
                i += 1
        return i
s=Solution()
s.removeElement([3,2,2,3],3)
