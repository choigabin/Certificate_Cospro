#몸무게가 큰 사람의 수를 구하는 함수 수정하기
def solution(weight, k):
    answer = 0
    for w in weight: #리스트의 길이만큼 포문 돌리기
        if w > k: #w가 k보다 크다면,
            answer += 1 #answer에 1 증가
    return answer

weights = [65, 70, 75, 80, 84]
ret = solution(weights, 70)
print(ret)