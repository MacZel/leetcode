class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr_max = 0
        curr_peak = 0
        for i in range(0, len(A)):
            if A[i] > curr_max:
                curr_max = A[i]
                curr_peak = i
        return curr_peak