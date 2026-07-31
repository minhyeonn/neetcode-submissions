class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+", "-", "*", "/"]
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            elif tokens[i] == "+":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1+n2)
            elif tokens[i] == "-":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1-n2)
            elif tokens[i] == "*":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1*n2)
            elif tokens[i] == "/":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(n1/n2))
        return stack[0]
