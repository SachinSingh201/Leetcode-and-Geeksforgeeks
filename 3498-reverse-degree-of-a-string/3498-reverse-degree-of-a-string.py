class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        pos = 1
        for ch in s:
            value = 123 - ord(ch)
            ans += value*pos
            pos+=1
        return ans

