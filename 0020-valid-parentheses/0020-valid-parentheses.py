class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        prt = {'(': ')' , '{' :'}', '[' :']'}
        for ch in s:
            if ch in prt:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if prt[top] != ch:
                    return False
        return not stack

            
        