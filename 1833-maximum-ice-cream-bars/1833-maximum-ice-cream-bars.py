class Solution(object):
    def maxIceCream(self, costs, coins):
        
        count = 0
        costs = sorted(costs)
        for num in costs:
            if num <= coins:
                count+=1
                coins-=num

        return count

        