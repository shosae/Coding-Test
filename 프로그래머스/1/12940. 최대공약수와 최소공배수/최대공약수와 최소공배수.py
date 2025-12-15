def solution(n, m):
    # 항상 n이 더 크도록 유지
    if n < m:
        n, m = m, n
    n_, m_ = n, m # 계산용
    
    #gcd
    while m_ >0:
        n_, m_ = m_, n_%m_

    return [n_, (n*m)// n_] # [gcd, lcm]