# class Solution(object):
#     def smallestNumber(self, n, t):
#         """
#         :type n: int
#         :type t: int
#         :rtype: int
#         """
     
#         for num in range(n,n+t):
#             x = 1
#             ans = num
#             while num:
#                 x *= num% 10
#                 num //= 10
#             if x% t == 0:
#                 return ans
            

class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            p=n
            pr=1
            while p>0:
                pr*=p%10
                p//=10
            if pr%t==0:return n
            n+=1
        
