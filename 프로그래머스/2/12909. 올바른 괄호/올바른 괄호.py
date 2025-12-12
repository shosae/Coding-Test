def solution(s):
    a = []

    if s[0] ==")":
        return False

    for c in s:
        if c == "(":
            a.append(c)
        else:
            if a:
                a.pop()
            else:
                return False

    return False if a else True