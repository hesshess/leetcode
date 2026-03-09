class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            print(i)
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k