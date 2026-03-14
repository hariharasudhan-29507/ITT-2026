class Solution(object):
    def strStr(self, haystack, needle):
        lens=len(needle)
        for i in range(0,len(haystack)):
           if  haystack[i:i+lens]==needle:
                return i
        return -1
s= Solution()
s.strStr("sadbutsad","sad")