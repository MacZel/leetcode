class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        countJewels = 0
        for stone in S:
            if stone in J:
                countJewels +=1
                
        return countJewels
