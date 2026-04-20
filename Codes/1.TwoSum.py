#Author - Hariharasudhan A
#brute force
class Solution:
    def twoSum(self, nums, target):
        res=[]
        # iterate through every element and add them and compare with target 
        for i in range(0,len(nums)): # num 1 iteration
            for j in range(i+1,len(nums)): # num 2 iteration
                if nums[i]+nums[j]==target: # if num1+num2 = target 
                    res.append(i) # insert the indices in to the array
                    res.append(j)
                    return res # return the indices
                    break            
nums=[2,7,11,15]
target=9
s=Solution()
res=s.twoSum(nums,target)
