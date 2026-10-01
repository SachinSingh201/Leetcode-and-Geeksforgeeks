class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(heights)-1
        left = 0
        maxarea = float('-inf')
        while left < right:
            currarea = (right-left) * min(heights[left],heights[right])
            maxarea = max(maxarea,currarea)
            if heights[left] < heights[right]:
                left+=1
            else:
                right -=1
        return maxarea

        