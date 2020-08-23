"""
Evaluate RPN expression: EPI 7.2
"""


def evaluate(RPN_expression):
    tokens = RPN_expression.split(',')
    stack = []
    operator = {
        '-': lambda x,y: x - y,
        '+': lambda x,y: x + y,
        '/': lambda x,y: x/y,
        '*': lambda x,y: x*y
    }
    for t in tokens:
        if t in operator:
            first_num = int(stack.pop())
            second_num = int(stack.pop())
            value = operator[t](first_num, second_num)
            stack.append(value)
        else:
            stack.append(t)

    return stack[-1]


print(evaluate('1,2,+,5,*'))
