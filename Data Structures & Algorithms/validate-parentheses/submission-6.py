class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False

        mapper = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for braket in s:
            if braket in ('(', '[', '{'):
                stack.append(braket)
            
            else:
                if not stack:
                    return False 

                if stack[-1] == mapper.get(braket):
                    stack.pop()
                else:
                    return False
        
        return  len(stack) == 0
        