# class Solution(object):
#     def removeCoveredIntervals(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         intervals.sort(key = [0])
#         queue = [intervals[0]]
#         i = 0
#         while i < len(intervals)-1:
#             n1 = intervals[i]
#             n2 = interva;s[i+1]
#             a = n1[0]
#             b = n1[-1]
#             c = n2[0]
#             d = n2[-1]
#             if not a <= c and not b<=d:
#                 intervals.pop(i+1)
#         return len(intervals)

        
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining = len(intervals)
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            current_end = intervals[i][1]
            
            if current_end <= prev_end:
                remaining -= 1
            else:
                prev_end = current_end
                
        return remaining
