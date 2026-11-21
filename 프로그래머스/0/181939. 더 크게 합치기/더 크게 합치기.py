def solution(a, b):
    answer = 0
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    if x > y:
        answer = x
    elif x < y:
        answer = y
    else :
        answer = x
    return answer