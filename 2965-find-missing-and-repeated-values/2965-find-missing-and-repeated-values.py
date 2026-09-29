class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
       
        n = len(grid) * len(grid) 
        sn = n*(n+1) //2
        s2n = n *(n+1) * (2*n+1) //6
        sgn = 0
        s2gn = 0

        for row in grid:
           for val in row:
               sgn += val
               s2gn += val*val 
                
        a = sn - sgn 
        b = (s2n - s2gn) // a

        missing = (a+b)//2
        repeating = missing - a


        return [repeating , missing]

 
    


