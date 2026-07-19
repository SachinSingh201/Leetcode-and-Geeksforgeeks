class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers = {"I":1, "V":5 ,"X":10 , "L":50,"C":100,"D":500,"M":1000}
        ans =0
        for i in range(len(s)-1) :
            if numbers.get(s[i]) >= numbers.get(s[i+1]):
                ans+= numbers.get(s[i])
            else:
                ans-= numbers.get(s[i])
        ans+= numbers.get(s[-1])
        return ans
        