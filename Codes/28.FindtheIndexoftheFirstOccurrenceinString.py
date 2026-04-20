# Author - Hariharasudhan A
class Solution(object):
    def strStr(self, haystack, needle):
        lens=len(needle) # len of substring
        for i in range(0,len(haystack)):# iterate till length of string
           if  haystack[i:i+lens]==needle: # if substring present in string 
                return i # return index
        return -1
s= Solution()
s.strStr("sadbutsad","sad")
