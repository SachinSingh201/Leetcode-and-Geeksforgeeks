from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        pos = {}
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    pos[(i, j)] = len(pos)

        target = (1 << len(pos)) - 1
        q = deque([(sx, sy, energy, 0, 0)])
        
       
        seen = {(sx, sy, 0): energy}

        while q:
            x, y, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if classroom[nx][ny] == 'X':
                    continue

                ne = e - 1
                nm = mask

                if classroom[nx][ny] == 'R':
                    ne = energy

                if (nx, ny) in pos:
                    nm |= 1 << pos[(nx, ny)]

                state = (nx, ny, nm)

                if state not in seen or seen[state] < ne:
                    seen[state] = ne
                    q.append((nx, ny, ne, nm, moves + 1))

        return -1