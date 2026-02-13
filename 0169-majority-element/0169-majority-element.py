class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        chrs = set(nums)
        for x in chrs:
           count[x] = 0
        for y in nums:
            count[y] += 1
            if count[y] > (len(nums) / 2):
                return y

        

