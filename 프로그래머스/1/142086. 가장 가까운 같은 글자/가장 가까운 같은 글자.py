def solution(s):
    dic = {}
    ans = []
    for i, c in enumerate(s):
        if c not in dic:
            dic[c] = i
            ans.append(-1)
        else:
            ans.append(i - dic[c])
            dic[c] = i
    return ans