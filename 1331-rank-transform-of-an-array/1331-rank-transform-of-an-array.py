class Solution(object):
    def arrayRankTransform(self, arr):
      
        unique_sorted = sorted(list(set(arr)))
        
       
        rank_map = {}
        for rank, val in enumerate(unique_sorted):
            rank_map[val] = rank + 1

        for i in range(len(arr)):
            arr[i] = rank_map[arr[i]]
            
        return arr
