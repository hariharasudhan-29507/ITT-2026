#Author - Hariharasudhan A
class Solution(object):
    	def removeDuplicates(self, nums):
            nums[:] = sorted(set(nums)) # set can't have duplicates
            return len(nums)
s=Solution()
s.removeDuplicates([1,1,2])
        
