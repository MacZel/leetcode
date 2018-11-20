class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        if strs:
            max_prefix_len = min([len(str) for str in strs])
        
            for index in range(max_prefix_len):
                strs_set = set([str[:index+1] for str in strs])
                if len(strs_set) <= 1:
                    ans = list(strs_set)[0]
                else:
                    break
        return ans
