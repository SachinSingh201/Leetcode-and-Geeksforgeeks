class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        num  = []
        while n != 0:
            num.append(n%10)
            n= n// 10
        if len(num)<2:
            return 0
        x1 = max(num)
        idx = num.index(x1)
        num.pop(idx)
        x2 = max(num)
        return x1*x2
        