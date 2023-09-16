
def evalRPN(tokens: List[str])  -> int:
    def bi_ops(token, a, b):
        match token:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return int(a / b)

        stack = []
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                num = bi_ops(token, a, b)
            finally:
                stack.append(num)
        return stack[0]
