def operation(n1, n2, sign):
    if sign == '+':
        res = n1 + n2
    elif sign == '-':
        res = n1 - n2
    elif sign == '*':
        res = n1 * n2
    else:
        res = n2 // n1
    return res


def basic_calc(st):
    stack = []

    priorities = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }

    for i in range(len(st)):
        if stack:
            if st[i] in priorities and stack[-1] in priorities and priorities[st[i]] > priorities[stack[1]]:
                num1 = int(st[i + 1])
                num2 = stack.pop()
                stack.append(operation(num1, num2, st[i]))
                while stack:
                    num1 = stack.pop()
                    sign = stack.pop()
                    num2 = stack.pop()
                    stack.append(operation(num1, num2, sign))
            else:
                stack.append(st[i])
        else:
            stack.append(st[i])
    return 0


if __name__ == '__main__':
    s = '3+2*2'
    basic_calc(s)
