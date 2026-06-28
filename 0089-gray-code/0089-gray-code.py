class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # ans = [0,1]
        # if n == 1:
        #     return ans
        res = []
        for x in range(0,2**n):
            res.append(x^x >>1)
        return res
        
      
        