class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        temp=0
        while(n>0):
            rem=n%10
            temp=(temp*10)+rem
            n//=10
        if x==temp:
            return True
        else:
            return False
s=Solution()
x=121
print(s.isPalindrome(x))