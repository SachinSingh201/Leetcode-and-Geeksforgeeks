class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # ans = 1
        # isneg = False
        # if n  < 0:
        #     n = abs(n)
        #     isneg = True
        # while n > 0 :
        #     ans *= x 
        #     n-=1
        # if isneg :
        #     return 1 / ans
        ans = x**n
        return ans

