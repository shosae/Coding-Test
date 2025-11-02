def solution(s):
    ss = [int(i) for i in s.split()]
    return f"{min(ss)} {max(ss)}"

