class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        target = sum(nums)-x
        if target < 0:
            return -1 
        left = 0
        maxLength = -1
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right]

            while currSum > target and left <= right:
                currSum -= nums[left]
                left+=1
            if currSum == target:
                maxLength = max(maxLength , right-left +1)

        return n - maxLength if maxLength != -1 else -1
