from typing import List


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

      
        size = 4 * n
        tree = [[0] * (k + 1) for _ in range(size)]

        def make_leaf(node, value):
            value %= k

            tree[node] = [0] * (k + 1)

            
            tree[node][value] = 1

            
            tree[node][k] = value

        def merge(left, right):
            res = [0] * (k + 1)

            left_prod = left[k]
            right_prod = right[k]

           
            res[k] = (left_prod * right_prod) % k

            
            for r in range(k):
                res[r] += left[r]

            for r in range(k):
                new_r = (left_prod * r) % k
                res[new_r] += right[r]

            return res

        def build(node, l, r):
            if l == r:
                make_leaf(node, nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                make_leaf(node, value)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

           
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

           
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        
        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            
            update(1, 0, n - 1, index, value)

            
            result = query(1, 0, n - 1, start, n - 1)

            
            ans.append(result[x])

        return ans