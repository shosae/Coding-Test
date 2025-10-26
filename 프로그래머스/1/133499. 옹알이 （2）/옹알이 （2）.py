def solution(babbling):
    result = 0
    cant = ["ayaaya", "yeye", "woowoo", "mama"]
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling: 
        skip_word = False
        for cnt in cant:
            if cnt in b:
                skip_word = True
                break
        if skip_word:
            continue 
        for c in can:
            b = b.replace(c, " ")
        b = b.replace(" ", "")
        if len(b) == 0:
            result += 1
            
    return result