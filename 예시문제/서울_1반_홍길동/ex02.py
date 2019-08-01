# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    # lst = [i for i in equation]
    lst = equation.split('+')
    for i in lst:
        if i == '':
            lst.remove(i)
    
    
    for i in range(len(lst)):
        if  '-' in lst[i]:
            idx=lst[i].index('-')
            if idx == 0 :
                lst[i] = -int(lst[i][1:])
                
            else:
                lst[i] = int(lst[i][:idx]) - int(lst[i][idx+1:])
            
    lst = list(map(int, lst))    
    result = sum(lst)

    return result








# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

