class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x11, y11, x22, y22 = rec2

       
        if x2 <= x11 or x22 <= x1:
            return False

        if y2 <= y11 or y22 <= y1:
            return False

        return True