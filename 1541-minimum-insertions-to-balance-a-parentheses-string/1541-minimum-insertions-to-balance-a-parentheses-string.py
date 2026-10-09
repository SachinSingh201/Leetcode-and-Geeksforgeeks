class Solution(object):
    def minInsertions(self, s):
        open = 0
        ans = 0

        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open += 1
            else:
                
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                   
                    ans += 1

                if open > 0:
                    open -= 1
                else:
                   
                    ans += 1

            i += 1

        
        ans += open * 2

        return ans