class Solution(object):
    
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start_j = int(math.sqrt(c))
        start_i = 0
        while start_i <= start_j:
            
            total = start_i * start_i + start_j * start_j
            
            if total == c:
                return 1
            if total > c:
                start_j = start_j - 1
            else:
                start_i = start_i + 1
            
        return 0
