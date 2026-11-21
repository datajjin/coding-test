def solution(a, b):
    answer = 0
    x = int(str(a) + str(b))
    y = 2 * a * b
    if x > y :
        answer = x
    elif x < y :
        answer = y
    else :
        answer = x
    return answer