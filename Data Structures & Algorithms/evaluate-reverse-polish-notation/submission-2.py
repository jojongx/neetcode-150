class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = None
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                num = stack.pop()
                match token:
                    case "+":
                        stack.append(stack.pop() + num)
                    case "-":
                        stack.append(stack.pop() - num)
                    case "*":
                        stack.append(stack.pop() * num)
                    case "/":
                        stack.append(int(stack.pop() / num))
        return stack[-1]
