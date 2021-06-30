#특정 값보다 작은 값을 차는 함수 수정하기
def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average: #i가 평균 미만이라면,
            cnt += 1 #cnt에 1 증가
    return cnt

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = solution(data)
print(ret)