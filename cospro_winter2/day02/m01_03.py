#학습 대상자를 구하는 함수 수정하기
def solution(scores):
    count = 0
    for s in range(len(scores)): #스코어 리스트의 길이만큼 포문 돌리기
        if scores[s] <= 200: #s가 200보다 작거나 같다면,
            count += 1 #count에 1 증가
    return count

scores = [100, 200, 300, 400]
ret = solution(scores)
print(ret)