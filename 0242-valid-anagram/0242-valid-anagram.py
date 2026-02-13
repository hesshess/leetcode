class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count={}
        for x in s:
            count[x] = count.get(x, 0) + 1

        for y in t:
            if y not in count:
                return False
            count[y] -= 1
            if count[y] == 0:
                del count[y]
        return len(count) == 0
        
        