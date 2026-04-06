class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculation_stack = []
        result = 0

        for token in tokens:
            # print(f"current calculation_stack are: {calculation_stack}")
            # print(f"current token is: {token}")

            if token in "+-*/":
                # The stack should have 2 numbers
                num2 = int(calculation_stack.pop())
                # print(f"num2 is: {num2}")

                num1 = int(calculation_stack.pop())
                # print(f"num1 is: {num1}")

                # Check the moment recent value
                if token == "+":
                    calculation_stack.append(num1 + num2)
                elif token == "-":
                    calculation_stack.append(num1 - num2)
                elif token == "*":
                    calculation_stack.append(num1 * num2)
                elif token == "/":
                    calculation_stack.append(num1 / num2)
            else:
                calculation_stack.append(token)
        result = int(calculation_stack.pop())
        return result
                    