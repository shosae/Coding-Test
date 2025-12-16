def solution(s):
    ans = ""
    tmp = ""
    num = {
        "zero": 0, "one": 1, "two": 2,"three": 3,
        "four": 4, "five": 5, "six": 6, "seven": 7,
        "eight": 8, "nine": 9,}
    
    for c in s:
        if c.isdigit():
            ans += c
        else:
            tmp += c

        if tmp in num:
            ans += str(num[tmp])
            tmp = ""

    return int(ans)