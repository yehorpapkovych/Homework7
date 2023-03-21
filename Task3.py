def make_operator(a, *args):
    result = 0
    for i in range(len(args)):
        if a == '+':
            result += args[i]
        if a == '-':
            if i == 0:
                result = args[i]
            else:
                result -= args[i]
        if a == '*':
            if i == 0:
                result = 1 * args[i]
            else:
                result = result * args[i]
    return result

print(make_operator('-', 5, 5, -10, -20))
