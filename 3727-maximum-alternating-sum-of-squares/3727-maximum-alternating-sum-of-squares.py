class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2

        nums.sort()
        i = 0
        j = len(nums)-1
        ans = 0
        while i < j:
            ans = ans+nums[j] - nums[i]
            j-=1
            i+=1
        if len(nums)%2 != 0:
            ans += nums[j]
            
        return ans
        