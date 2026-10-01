# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         intervals.sort(key = lambda x : x [0])
#         ans = []
#         if len(intervals) < 2:
#             return intervals
#         x = intervals[0][0]
#         y = intervals[0][1]

#         for i in range(1,len(intervals)):
#             nx ,ny = intervals[i][0] , intervals[i][1]
#             if nx <= y and x < nx :
#                 ans.append([x,ny])
#                 y = ny 
#             else:
#                 ans.append([x,y])
#                 x = nx 
#                 y = ny 
#         return ans


class Solution(object):
    def merge(self, intervals):
       
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd,end)
            else:
                res.append([start,end])
        return res            
        
