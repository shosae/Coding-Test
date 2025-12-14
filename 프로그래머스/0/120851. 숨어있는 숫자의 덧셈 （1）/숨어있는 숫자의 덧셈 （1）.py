def solution(m):
    ans = 0
    for i in m:
        if i.isdigit():
            ans += int(i)
    return ans