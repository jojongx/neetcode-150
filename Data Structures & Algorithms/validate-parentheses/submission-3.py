class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in my_dict:
                if stack and stack[-1] == my_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False