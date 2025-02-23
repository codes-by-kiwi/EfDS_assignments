import sys

def rpn(tokens):
    math_ops = ['+','-','*','/']
    stack = []

    for token in tokens:
        if token not in math_ops:
            try:
                if '.' in token:
                    number = float(token)
                else:
                    number = int(token)
                stack.append(number)

            except ValueError:
                raise ValueError(f"Could not convert string to float: '{token}'")

        else:
            if len(stack) < 2:
                raise RuntimeError(f"Not enough arguments for {token} operator.")
            number2 = stack.pop()
            number1 = stack.pop()
    
            if token == '+':
                stack.append(number1+number2)
            elif token == '*':
                stack.append(number1*number2)
            elif token == '-':
                stack.append(number1-number2)
            elif token == '/':
                if number2 == 0:
                    raise RuntimeError("Error: Division by zero.")
                stack.append(number1/number2)
            
    if len(stack) !=1:
        raise RuntimeError("Not enough operators; too many elements on remained on stack.")
    return stack[0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    tokens = sys.argv[1:]

    try:
        result = rpn(tokens)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

