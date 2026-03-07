class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mid = 0
        for x in range(1, len(numbers)):
            val = target - numbers[x-1]
            low, high = x, len(numbers)
            while low <= high:        
                mid = (low + 1 + high) // 2
                print(numbers[low-1],numbers[mid-1],numbers[high-1],val)
                if numbers[mid-1] == val:
                    return [x, mid]
                elif numbers[mid-1] > val:
                    high = mid -1
                else:
                    low = mid +1



            



        