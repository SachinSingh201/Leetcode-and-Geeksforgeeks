# class Solution(object):

#     def findKthSmallest(self, coins, k):

#         values = set()

#         for coin in coins:

#             multiple = coin

#             for _ in range(k):
#                 values.add(multiple)
#                 multiple += coin

#         values = sorted(values)

#         return values[k - 1]
    
   

    
class Solution:
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        coins.sort()

        useful = []

        for c in coins:
            redundant = False

            for x in useful:
                if c % x == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(c)

        coins = useful
        n = len(coins)

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                L = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        if L > x:
                            valid = False
                            break

                if valid:
                    if bits % 2 == 1:
                        total += x // L
                    else:
                        total -= x // L

            return total

        left = 1
        right = min(c * k for c in coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left