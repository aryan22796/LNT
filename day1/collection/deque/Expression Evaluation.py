# Evaluate an expression in Reverse Polish Notation (RPN) using a deque.

from collections import deque

def evaluate_rpn(expression):
    stack = deque()
    
    for token in expression:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Ensure integer division
    
    return stack.pop()

# Test the function
print(evaluate_rpn(["2", "1", "+", "3", "*"]))  # 9
print(evaluate_rpn(["4", "13", "5", "/", "+"]))  # 6
