class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = []
        d = 0
        for ch in seq:
            if ch =='(':
                d+=1
                ans.append(d%2)
            else:
                ans.append(d%2)
                d-=1
        return ans
