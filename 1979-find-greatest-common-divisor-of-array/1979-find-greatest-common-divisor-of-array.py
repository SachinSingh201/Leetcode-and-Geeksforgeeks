class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a  = max(nums)
        b = min(nums)
        while  b!= 0:
            temp = b
            b = a%b
            a = temp
        return a

        
        