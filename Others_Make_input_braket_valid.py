'''Input lee(c)(ode))
Output lee(c)(ode)'''


def make_input_brackets_valid(s):
    s_stack = []
    for i in range(len(s)):
        if s[i] == '(':
            s_stack.append(i)
        elif s[i] == ')':
            if len(s_stack) != 0 and s[s_stack[-1]] == '(':
                s_stack.pop()
            else:
                s_stack.append(i)

    for i in s_stack:
        s = s[:i]+''+s[i+1:]
    print(s)
inp = "leet((co(de))))"
make_input_brackets_valid(inp)
