class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        matched_list = []
        
        for word in words:
            curr_map = {}
            do_match = True
            for letter, mapping in zip(word, pattern):
                if curr_map.get(letter, False):
                    if curr_map[letter] != mapping: #or mapping in curr_map.values():
                        do_match = False
                        break
                else:
                    if mapping in curr_map.values():
                        do_match = False
                        break
                    else:
                        curr_map[letter] = mapping
            if do_match:
                matched_list.append(word)
        return matched_list