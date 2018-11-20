class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        neg = -1 if x < 0 else 1
        x = abs(x)
        
        ans = 0
        while x != 0:
            ans = ans * 10 + x % 10
            x = int(x / 10)
            
        ans *= neg
        
        lim = 2**31
        if ans >= -lim and ans <= lim-1:
            return ans
        else:
            return 0
