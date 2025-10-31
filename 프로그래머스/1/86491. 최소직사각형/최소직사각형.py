def solution(sizes):
    for s in sizes:
        s.sort()
    i, j = zip(*sizes)
    return max(i) * max(j)