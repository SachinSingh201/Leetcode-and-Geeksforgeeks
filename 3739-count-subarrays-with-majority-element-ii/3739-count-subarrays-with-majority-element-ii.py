from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums, target):
        arr = [1 if x == target else -1 for x in nums]

        prefix = [0]
        s = 0

        for x in arr:
            s += x
            prefix.append(s)

        vals = sorted(set(prefix))

        bit = [0] * (len(vals) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            ans = 0
            while i > 0:
                ans += bit[i]
                i -= i & -i
            return ans

        ans = 0

        for p in prefix:
            idx = bisect_left(vals, p) + 1
            ans += query(idx - 1)
            update(idx)

        return ans