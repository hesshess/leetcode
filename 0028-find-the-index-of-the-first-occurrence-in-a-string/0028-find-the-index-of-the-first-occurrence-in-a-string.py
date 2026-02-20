class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        save = []
        for x in range(len(haystack)):
            if haystack[x] == needle[0]:
                save.append(x)
        for y in save:
            if haystack[y:(y+len(needle))] == needle:
                return y
             
        return -1


            
