def is_right(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    if len(stack) != 0:
        return False
    return True


def find_u_v(s):
    i = 0
    cnt1, cnt2 = 0, 0
    while cnt1 == 0 or cnt1 != cnt2:
        if s[i] == '(':
            cnt1 += 1
        elif s[i] == ')':
            cnt2 += 1
        i += 1
    return s[:i], s[i:]


def solution(p):
    if p == '':
        return p

    u, v = find_u_v(p)

    if is_right(u):
        return u + solution(v)
    else:
        reversed_u = ''
        for c in u[1:-1]:
            if c == '(':
                reversed_u += ')'
            elif c == ')':
                reversed_u += '('
        return '(' + solution(v) + ')' + reversed_u

for p in ["(()())()",")(","()))((()"]:
    print(p,'->', solution(p))
