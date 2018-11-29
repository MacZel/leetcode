class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        N_rows = len(A)
        N_cols = len(A[0])
        # If A is a square matrix, transpose in place
        if N_rows == N_cols:
            for row_i in range(N_rows):
                for col_i in range(row_i+1, N_rows):
                    temp = A[row_i][col_i]
                    A[row_i][col_i] = A[col_i][row_i]
                    A[col_i][row_i] = temp
            return A
        # otherwise create new matrix
        else:
            A_T = []
            for i in range(N_cols):
                row_T = []
                for row in A:
                    row_T.append(row[i])
                A_T.append(row_T)
            return A_T