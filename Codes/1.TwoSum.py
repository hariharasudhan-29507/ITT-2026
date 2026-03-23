class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    return res
                    break            
nums=[2,7,11,15]
target=9
s=Solution()
res=s.twoSum(nums,target)
