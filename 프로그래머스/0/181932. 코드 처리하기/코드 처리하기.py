def solution(code):
    mode = 0
    ret =''
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = 1 - mode
        elif code[idx] != "1":
            if mode == 0 and idx % 2 == 0 :
                ret += code[idx]
            elif mode == 1 and idx % 2 == 1 :
                ret += code[idx]
    if ret == '':      
        return "EMPTY"
    return ret