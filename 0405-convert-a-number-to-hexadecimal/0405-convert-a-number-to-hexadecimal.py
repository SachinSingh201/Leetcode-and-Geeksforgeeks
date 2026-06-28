class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        digits = "0123456789abcdef"
        if num < 0:
            num += 2**32
        ans = ""
        while num:
            rem = num % 16
            num = num//16
            ans+=digits[rem]
        return ans[::-1]

        
        