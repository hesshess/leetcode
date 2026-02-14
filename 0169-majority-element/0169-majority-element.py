class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        cnt = 0
        for x in nums:
            if cnt == 0:
                maj = x
                cnt += 1
            elif x == maj:
                cnt += 1
            else:
                cnt -= 1
        return maj