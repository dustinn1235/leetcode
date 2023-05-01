class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(y+x)
            elif token == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif token == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(y*x)
            elif token == "/":
                x = stack.pop()
                y = stack.pop()
                div = y / x
                if div < 0:
                    stack.append(math.ceil(div))
                else:
                    stack.append(math.floor(div))
            else:
                stack.append(int(token))
        return stack.pop()