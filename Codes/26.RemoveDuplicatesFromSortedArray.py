class Solution(object):
    	def removeDuplicates(self, nums):
            nums[:] = sorted(set(nums))
            return len(nums)
s=Solution()
s.removeDuplicates([1,1,2])
        