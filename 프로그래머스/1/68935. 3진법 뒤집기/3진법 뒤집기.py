def solution(n):
    cnt = 0
    ans = 0
    tmp = []
    while n>0:
        n, r = divmod(n,3)
        tmp.append(r)

    for k in tmp[::-1]:
        ans += (3**cnt) * k
        cnt += 1
    return ans