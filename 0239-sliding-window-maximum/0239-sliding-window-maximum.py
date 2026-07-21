from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums:
            return []

        queue = deque()  
        ans = []

        for i in range(len(nums)):

            
            while queue and queue[0] <= i - k:
                queue.popleft()

            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            
            queue.append(i)

           
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans