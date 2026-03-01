class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = round((high - low) / 2 + low)
            print(mid)
            if nums[mid] > target:
                high = mid - 1
                continue
            elif nums[mid] < target:
                low = mid + 1
                continue
            else: 
                return mid
        return -1