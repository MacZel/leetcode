class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        # Reduce the matrix diagonally
        for i in range(int(N/2)):
            
            # Go thorugh every node at edge
            for j in range(i, N-i-1):
                copy_curr = matrix[i][j]
                copy_next = None 
                
                # Perform rotation cycle
                for k in range(4):
                    t = i
                    i = j
                    j = N - t - 1
                    copy_next = matrix[i][j]
                    matrix[i][j] = copy_curr
                    copy_curr = copy_next
        
        return