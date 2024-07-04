class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        op = ["+","-","*","/"]
        for i in tokens:
            if i not in op:
                stack.append(i)
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if i == "+":
                    stack.append(int(n2) + int(n1))
                if i == "-":
                    stack.append(int(n2) - int(n1))
                if i == "*":
                    stack.append(int(n2) * int(n1))
                if i == "/":
                    stack.append(int(n2) / int(n1))
        return int(stack[0])
                