class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        s=""
        lens=len(strs)
        i=0
        while i < len(strs[0]):
            if strs[0][i] == strs[lens-1][i]:
                s+=strs[0][i]
            else:
                break
            i=i+1
        return s
        
s=Solution()
strs=["flower","flight","flow"]
s.longestCommonPrefix(strs)