class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def sq (x: int) -> int:
            return x ** 2
        result = [0] * (len(nums))
        
        low, high = 0, len(nums)-1
        pos = len(nums)-1

        while low <= high:
            sq_low = sq(nums[low])
            sq_high = sq(nums[high])
            if sq_low > sq_high:
                result[pos] = sq_low
                low += 1
            else:
                result[pos] = sq_high
                high -= 1
            pos -= 1
        return result
            

                

        