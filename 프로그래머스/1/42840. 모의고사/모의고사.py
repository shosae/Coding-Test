def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    correct =[0, 0, 0]

    for i, a in enumerate(answers):
        if a == stu1[i%len(stu1)]:
            correct[0] += 1
        if a == stu2[i%len(stu2)]:
            correct[1] += 1
        if a ==stu3[i%len(stu3)]:
            correct[2] += 1

    winner = max(correct)
    
    return [i+1 for i, v in enumerate(correct) if v == winner]