class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n not in '+/-*':
                stack.append(n)
            elif n == '+':
                number1 = int(stack.pop())
                number2 = int(stack.pop()) 
                stack.append(number2 + number1)
            elif n == '-':
                number1 = int(int(stack.pop()))
                number2 = int(stack.pop()) 
                stack.append(number2 - number1)
            elif n == '/':
                number1 = int(stack.pop())
                number2 = int(stack.pop()) 
                stack.append(int(number2 / number1))
            elif n == '*':
                number1 = int(stack.pop())
                number2 = int(stack.pop()) 
                stack.append(number2 * number1)
        return int(stack[0])