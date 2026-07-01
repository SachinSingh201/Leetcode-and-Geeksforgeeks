from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        q = deque([(root, 0)])
        ans = 0

        while q:
            size = len(q)
            first = q[0][1]
            last = q[-1][1]

            ans = max(ans, last - first + 1)

            for _ in range(size):
                node, idx = q.popleft()

                
                idx -= first

                if node.left:
                    q.append((node.left, 2 * idx + 1))

                if node.right:
                    q.append((node.right, 2 * idx + 2))

        return ans