def solution(survey, choices):
    KAKAO = {"R":0,"T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    ans = ""
    for s, score in zip(survey, choices):
        if score - 4 <= 0:
            KAKAO[s[0]] += abs(score-4)
        else:
            KAKAO[s[1]] += abs(score-4)
    
    types = ["RT", "CF", "JM", "AN"]
    
    for t in types:        
        if KAKAO[t[0]] >= KAKAO[t[1]]:
            ans += t[0]
        else:
            ans += t[1]
            
    return ans        