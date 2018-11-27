class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hamming_dist = 0
        
        pos_x = bin(x)[2:].zfill(31)
        pos_y = bin(y)[2:].zfill(31)
        
        for i in range(31):
            if pos_x[i] != pos_y[i]:
                hamming_dist +=1
        
        return hamming_dist