from collections import Counter
def solution(p, c):
    cp = Counter(p)
    cc = Counter(c)
    diff = cp - cc
    return list(diff.keys())[0]