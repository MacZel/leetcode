class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        A.sort()
        counter=0
        for index in range(1,N):
            if A[index] <= A[index-1]:
                temp = A[index]
                A[index] = A[index-1] + 1
                counter += A[index-1] + 1 - temp
        return counter