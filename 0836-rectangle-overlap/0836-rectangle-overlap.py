class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x11, y11, x22, y22 = rec2

        
        left = max(x1, x11)
        right = min(x2, x22)

        bottom = max(y1, y11)
        top = min(y2, y22)

        
        if left >= right or bottom >= top:
            return False
        return True