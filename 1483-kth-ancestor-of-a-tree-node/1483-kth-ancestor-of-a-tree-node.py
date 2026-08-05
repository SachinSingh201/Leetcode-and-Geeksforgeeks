class TreeAncestor(object):

    def __init__(self, n, parent):

        self.LOG = 16

        while (1 << self.LOG) <= n:
            self.LOG += 1

        self.up = [[-1] * self.LOG for _ in range(n)]

        # 2^0 ancestor
        for i in range(n):
            self.up[i][0] = parent[i]

        # Build sparse table
        for j in range(1, self.LOG):
            for i in range(n):

                prev = self.up[i][j - 1]

                if prev != -1:
                    self.up[i][j] = self.up[prev][j - 1]

    def getKthAncestor(self, node, k):

        bit = 0

        while k > 0:

            if k & 1:

                node = self.up[node][bit]

                if node == -1:
                    return -1

            k >>= 1
            bit += 1

        return node