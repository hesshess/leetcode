class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        output = []
        while i < len(word1) and i < len(word2):
            output.append(word1[i])
            output.append(word2[i])
            i += 1
        output.append(word1[i:])
        output.append(word2[i:])
        return "".join(output)
        