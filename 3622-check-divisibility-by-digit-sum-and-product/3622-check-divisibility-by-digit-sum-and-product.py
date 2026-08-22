class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sumX = 0
        multipleX = 1
        num = n 
        while num:
            digit = num%10
            sumX+= digit
            multipleX *= digit
            num = num//10
        
        return (n % (sumX + multipleX) == 0)
        