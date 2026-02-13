class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for x in nums:
            if not x in seen:
                seen.add(x)
            else:
                return True
        return False
        