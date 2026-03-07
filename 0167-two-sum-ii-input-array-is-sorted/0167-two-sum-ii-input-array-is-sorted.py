class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
                curr = numbers[low] + numbers[high]
                if curr == target:
                    return [low+1, high+1]
                elif curr < target:
                    low += 1
                else:
                    high -= 1