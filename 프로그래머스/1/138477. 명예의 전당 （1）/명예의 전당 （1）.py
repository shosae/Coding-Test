import heapq

def solution(k, score):
    table = []
    result = []
    for s in score:
        heapq.heappush(table, s)
        
        if len(table) > k:
            heapq.heappop(table)
        
        result.append(table[0])

    return result