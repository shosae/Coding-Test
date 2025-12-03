def solution(citations):
    for idx, c in enumerate(sorted(citations, reverse=True)):
        if c < idx+1:
            return idx
    return len(citations)