def solution(s):
    ss = sorted([int(i) for i in s.split()])
    return f"{ss[0]} {ss[-1]}"