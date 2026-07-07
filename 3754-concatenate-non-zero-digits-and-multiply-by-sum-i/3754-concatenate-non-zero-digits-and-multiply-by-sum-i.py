class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        strN = str(n)
        num = ""
        sumX = 0
        for x in strN:
            if x !="0":
                num+=x
                sumX+= int(x)
        return int(num)*sumX
        

        