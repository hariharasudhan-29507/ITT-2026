# Author - Hariharasudhan A
class Solution:
    def isPalindrome(self, x) :
        n=x # temproaruy copy
        temp=0 
        while(n>0):
            rem=n%10 # store last digit
            temp=(temp*10)+rem # reverse it 
            n//=10 # eliminate last digit
        if x==temp:
            return True
        else:
            return False
s=Solution()
x=121
print(s.isPalindrome(x))
