class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        answer = {}
        for i in range(n):
            while stack and nums2[i] > stack[-1]:
                prev = stack.pop()
                answer[prev] = nums2[i]
            stack.append(nums2[i])
        
        while stack:
            prev = stack.pop()
            answer[prev] = -1

        return [answer[num] for num in nums1]

