#Author - Hariharasudhan A
class Solution(object):
    def generateParenthesis(self, n):
        stack=[]# empty stack
        res=[]# empty result array
        
        def backTracking(countO,countC):
            '''
            countO - count of "("
            countC - count of ")"
            '''
            if countO==countC==n:
                res.append("".join(stack)) # joins the elements in the stack as a single string and we are inserting in result array

            # main condition for placing a ")" is when countC < countO ,i.e ((( then we can place a ) , if ()) then we cant place a )
            if countO < n: # for open parenthesis "(
                stack.append("(")
                backTracking(countO+1,countC)
                stack.pop() #c cleaning the stack
            if countC < countO: # for close parenthesis ")"
                stack.append(")")
                backTracking(countO,countC+1)
                stack.pop() # cleaning the stack
        backTracking(0,0)
        return res
