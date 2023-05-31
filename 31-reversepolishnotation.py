class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: 
            return 


        operator = tokens.pop()

        if not tokens: 
            return int(operator)

        if tokens[-1] not in '+-*/':
            operand2 = tokens.pop()
        else:
            operand2 = self.evalRPN(tokens)

        if tokens[-1] not in '+-*/':
            operand1 = tokens.pop()
        else:
            operand1 = self.evalRPN(tokens)

        if operator == "+":
            return int(operand1) + int(operand2)
        elif operator == "-":
            return int(operand1) - int(operand2)
        elif operator == "*":
            return int(operand1) * int(operand2)
        else:
            return int(float(operand1) / int(operand2))