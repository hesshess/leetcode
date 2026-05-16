class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', ']':'[', '}':'{'}

        for ch in s :
            if ch in pair:
                if not stack or stack.pop() != pair[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0