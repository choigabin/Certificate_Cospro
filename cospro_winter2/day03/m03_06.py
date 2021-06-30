#문자열 내 정수들의 총합 구하는 함수 빈칸 채우기
def solution(string):
    answer = 0
    number = 0
    s = string + '' #string을 char 타입으로
    for c in s:
        if '0' <= c and c <= '9': #c가 0보다 크거나 같고, 9보다 작거나 같다면,
            print(c, int(c)) #c와 int로 형변환한 c 출력
            number = number * 10 + int(c)
        else:
            answer += number
            number = 0
    return answer

string = "12 korean34"
ret = solution(string)
print(ret)