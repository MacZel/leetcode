class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows > 1:
            wordMatrix = []
            
            while s:
                vertical = s[:numRows]
                diagonal = s[numRows:2*(numRows-1)][::-1]
                diagonal = (numRows - len(diagonal) - 1) * " " + diagonal
                wordMatrix.append(vertical) if vertical else None
                wordMatrix.append(diagonal) if diagonal else None
                s = s[2*(numRows-1):]
                
            ans = ""
            for row_i in range(numRows):
                for word in wordMatrix:
                    ans += word[row_i:row_i+1]
            ans = ans.replace(" ", "")
            return ans
        else:
            return s