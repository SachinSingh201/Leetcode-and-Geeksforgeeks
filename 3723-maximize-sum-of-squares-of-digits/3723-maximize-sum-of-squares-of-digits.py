
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > num * 9:
            return ""

        result = []

        for _ in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        return ''.join(result)
