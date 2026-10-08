class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = deque()
        ans = ""
        openCount = 0
        for ch in s:
            q.append(ch)
            if ch =='(':
                openCount+=1
            elif ch == ')':
                openCount-=1
            if openCount == 0:
                q.popleft()
                q.pop()
                ans+= "".join(q)
                q = deque()
        return ans
            
            
            

        