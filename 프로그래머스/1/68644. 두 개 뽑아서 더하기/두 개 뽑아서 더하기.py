import itertools 

def solution(numbers):
    return sorted({a + b for a, b in itertools.combinations(numbers, 2)})