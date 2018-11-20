class Solution:
    def intToRoman(self, num):
        """
        :type num: int <1, 3999>
        :rtype: str
        """
        if num < 1 or num > 3999:
            return None
        
        int2roman = [
            ['I', 'V'],
            ['X', 'L'],
            ['C', 'D'],
            ['M'],
        ]
        ans = ''
        for i in range(4):
            digit = int(num % 10)
            num /= 10
            pre = ''
            if digit < 4:
                pre = digit * int2roman[i][0]
            elif digit == 4:
                pre = int2roman[i][0] + int2roman[i][1]
            elif digit < 9:
                pre = int2roman[i][1] + (digit % 5) * int2roman[i][0]
            else:
                pre = int2roman[i][0] + int2roman[i+1][0]
            ans = pre + ans
            
        return ans
