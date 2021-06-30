#거리차이를 구하는 함수 빈칸 채우기
def solution(a, b):
    answer = 0
    diff = (b-a) if a < b else a - b
    answer = 10 / diff #시간 = 거리 / 속력
    return answer*60 #초

a = 10
b = 12
ret = solution(a, b)
print(ret)