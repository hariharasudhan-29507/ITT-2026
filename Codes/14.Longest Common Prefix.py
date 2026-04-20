#Author - Hariharasudhan A
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort() # ['flight', 'flow', 'flower'] 
        '''
        it is enough to compare with 'flow' as 'flow' is in 'flower'
        sorting the array helps us to arrange the substrings 
        '''
        s="" 
        lens=len(strs)
        i=0
        # traverse through each and every character parallely 
        while i < len(strs[0]):
            if strs[0][i] == strs[lens-1][i]:
                s+=strs[0][i]
            else:
                break
            i=i+1
        return s # return the longest common prefix on array 
        
s=Solution()
strs=["flower","flight","flow"]
print(s.longestCommonPrefix(strs))
