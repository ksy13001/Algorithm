class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                n = int(token)
                stack.append(n)
            except ValueError:
                y, x = stack.pop(), stack.pop()
                if token == "+":
                    temp = x + y
                elif token == "-":
                    temp = x - y
                elif token == "*":
                    temp = x * y
                elif token == "/":
                    temp = int(x / y)
                stack.append(temp)
        return stack[0]
            
        
