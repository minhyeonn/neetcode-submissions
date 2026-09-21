class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] in op:
                a = stack.pop()
                b = stack.pop()
                if tokens[i]=='+':
                    stack.append(b+a)
                elif tokens[i]=='-':
                    stack.append(b-a)
                elif tokens[i]=='*':
                    stack.append(b*a)
                elif tokens[i]=='/':
                    stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]