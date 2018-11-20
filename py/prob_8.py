class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        LIMIT = 2**31
        INT_MIN = -LIMIT
        INT_MAX = LIMIT -1
        
        str = str.lstrip(" ")
        ans = 0
        signmap = dict([(43, 1), (45, -1)])
        sign = 1
        
        if str and ord(str[0]) in [43, 45]:
            sign = signmap[ord(str[0])]
            str = str[1:]
        str = str.lstrip("0")
        
        while str and ord(str[0]) != 32:
            if ord(str[0]) >= 48 and ord(str[0]) <= 57:
                ans *= 10
                ans += int(str[0])
                str = str[1:]
            else:
                break
        ans *= sign
        
        if ans < INT_MIN:
            return INT_MIN
        elif ans > INT_MAX:
            return INT_MAX
        else:
            return ans
