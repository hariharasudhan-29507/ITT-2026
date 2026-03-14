class Solution:
    def findMaxConsecutiveOnes(self, nums) :
        t=0
        c=0
        for num in (nums):
            if num==1:
                c+=1
                if c>t:
                    t=c
            else:
                c=0
        return t
                
            

        