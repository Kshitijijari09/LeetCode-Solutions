class Solution:
    def isValid(self, s: str) -> bool:
        #to remember check for the ending parenthesis and add to stack once you find it start poping the stack and in the end if the stack is empty  return true else false.
        dic = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        } 
        stack = []
        
        for ch in s:
            if ch in dic:
                if stack and stack[-1] == dic[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
           
            
        return True if not stack else False