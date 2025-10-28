def solution(d, budget):
    count = 0
    for s in sorted(d):
        if s <= budget:
            budget -= s
            count += 1
    return count