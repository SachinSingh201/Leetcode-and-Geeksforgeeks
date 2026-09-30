class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        currSum =0
        for num in nums:
            currSum += num
            if currSum > ans:
                ans = currSum
            if currSum < 0:
                currSum = 0
        return ans
            

        