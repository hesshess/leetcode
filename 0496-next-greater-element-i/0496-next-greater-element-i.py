class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_g = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_g[prev] = num
            stack.append(num)
        
        while stack:
            prev = stack.pop()
            next_g[prev] = -1
        
        return [next_g[num] for num in nums1 ]
        