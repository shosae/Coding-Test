"""
1. n < n+1 자연수
2. n, n+1의 2진수 변환 1의 개수가 같음
3. n의 다음 큰 숫자는 1,2를 만족하는 가장 작은 수
2진수 변환 후 1의 개수를 비교
"""
def solution(n):
    one = bin(n)[2:].count('1')
    want = 0
    a = n
    while(want != one):
        a += 1
        want = bin(a)[2:].count('1')
    return a