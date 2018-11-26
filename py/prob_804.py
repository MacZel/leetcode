class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseMap = [".-","-...","-.-.","-..",".",
                    "..-.","--.","....","..",".---",
                    "-.-",".-..","--","-.","---",
                    ".--.","--.-",".-.","...","-",
                    "..-","...-",".--","-..-","-.--",
                    "--.."]
        morseWords = []
        for word in words:
            morseWord = ''
            for letter in word:
                morseWord += morseMap[ord(letter) - 97]
            morseWords.append(morseWord)
        different_transormations = len(set(morseWords))
        return different_transormations
