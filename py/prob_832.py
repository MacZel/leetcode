class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(A)
        for i in range(N):
            A[i] = A[i][::-1]
            for j in range(N):
                A[i][j] = 1 if A[i][j] == 0 else 0
        return A
