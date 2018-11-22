class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}
        for string in strs:
            string_sorted = "".join(sorted(string))
            if string_sorted not in anagram_groups.keys():
                anagram_groups[string_sorted] = [string]
            else:
                anagram_groups[string_sorted].append(string)
        return list(anagram_groups.values())