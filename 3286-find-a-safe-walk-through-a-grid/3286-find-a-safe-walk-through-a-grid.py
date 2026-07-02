from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        rTot = len(grid)
        cTot = len(grid[0])
        destR, destC = rTot - 1, cTot - 1
    
        minDmg = [[float('inf')] * cTot for _ in range(rTot)]
        minDmg[0][0] = grid[0][0]
        
 
        dq = deque([(0, 0)])
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while dq:
            currR, currC = dq.popleft()
         
            if currR == destR and currC == destC:
                return minDmg[currR][currC] < health
                
            for rOff, cOff in offsets:
                nextR, nextC = currR + rOff, currC + cOff
                
                if 0 <= nextR < rTot and 0 <= nextC < cTot:
                    nextGridVal = grid[nextR][nextC]
                    nextDmg = minDmg[currR][currC] + nextGridVal
                    
                  
                    if nextDmg < minDmg[nextR][nextC] and nextDmg < health:
                        minDmg[nextR][nextC] = nextDmg
                        
                     
                        if nextGridVal == 0:
                            dq.appendleft((nextR, nextC))
                        else:
                            dq.append((nextR, nextC))
                            
        return minDmg[destR][destC] < health
