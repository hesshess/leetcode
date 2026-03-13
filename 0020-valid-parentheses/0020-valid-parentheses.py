class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            else:
                if len(stack) > 0:
                    y = stack.pop()
                    if x == ')':
                        if y != '(':
                            return False
                    if x == ']':
                        if y != '[':
                            return False
                    if x == '}':
                        if y != '{':
                            return False
                else:
                    return False
        return len(stack) == 0