class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        out_list = []
        low = 0
        high = len(S)
        for char in S:
            if char == 'I':
                out_list.append(low)
                low += 1
            elif char == 'D':
                out_list.append(high)
                high -= 1
        out_list.append(low)
        return out_list