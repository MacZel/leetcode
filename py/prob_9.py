class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        copy_x = x
        
        if x < 0:
            return False
        else:
            reversed_x = 0
            while x != 0:
                reversed_x = reversed_x * 10 + x % 10
                x = int(x / 10)
        
            if copy_x == reversed_x:
                return True
            else:
                return False
