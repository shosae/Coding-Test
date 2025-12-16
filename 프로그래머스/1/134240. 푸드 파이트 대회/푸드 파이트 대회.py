def solution(food):
    left = []
    for i, f in enumerate(food):
        amount = f//2
        if amount > 0:
            left.append(str(i)*amount)
    return ''.join(left + ["0"] + left[::-1])