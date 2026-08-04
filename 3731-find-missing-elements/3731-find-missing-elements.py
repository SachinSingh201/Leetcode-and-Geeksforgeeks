class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minNum = min(nums)
        maxNum = max(nums)
        ans = []

        for num in range(minNum,maxNum):
            if num not in nums:
                ans.append(num)
        return ans
        