# class Solution(object):
#     def sequentialDigits(self, low, high):
#         """
#         :type low: int
#         :type high: int
#         :rtype: List[int]
#         """
       
#         lowlen = len(str(low))
#         num = 0
#         for  j in range(lowlen+1):
#             num = num*10 + j
#         ans = [num]
#         start = num

#         while num < high:
#             num = num % low
#             lastdigit = num%10
#             if lastdigit <9 :
#                 num = num*10 + lastdigit + 1
#             else:
#                 low = low*10
#                 num = start*10 + len(str(low))
#                 start = num 
#             ans.append(num)
#         return ans[:-1:]

class Solution(object):
    def sequentialDigits(self, low, high):
        
        ans = []
        digits = "123456789"
        
        low_len = len(str(low))
        high_len = len(str(high))
        
      
        for length in range(low_len, high_len + 1):
           
            for start in range(10 - length):
                sub_str = digits[start : start + length]
                num = int(sub_str)
                

                if low <= num <= high:
                    ans.append(num)
                    
        return ans

        