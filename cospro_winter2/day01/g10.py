#특정 값보다 작은 값을 찾는 함수 수정하기
def solution(data):
    total = sum(data)
    #평균은 전체의 합 / data 리스트의 길이
    average = total / len(data)
    cnt = 0
    for d in data:
        #d가 average보다 작거나 같으면,
        if d <= average:
            #cnt 1 증가
            cnt += 1
    return cnt

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = solution(data)
print("함수의 반환값은 ", ret, "입니다.")