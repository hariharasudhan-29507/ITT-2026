
class Solution(object):
    def isValid(self, s):
        # create all possible types 
        mapping = {')': '(', '}': '{', ']': '['}
        stack = [] # empty stack
        
        for char in s:
            if char in mapping.values(): # only for opening brackets 
                stack.append(char) # push every fresh element
            elif char in mapping: # only for closing brackets 
                if not stack or mapping[char] != stack.pop(): 
                    '''
                    if stack doesnot exits / key doesnot match with pair then false 
                    '''
                    return False
        '''
        if stack is empty - True // key : pairs matched and every pushed element is popped
        if not - False // key : pairs not matched and every pushed element is not popped
        '''
        return not stack 
