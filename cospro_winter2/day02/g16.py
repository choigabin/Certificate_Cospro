#배열에서 k보다 큰 사람
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height: #키 배열의 길이만큼 포문 돌리기
        if h > k: #h가 k보다 크다면,
            answer += 1 #answer에 1 증가
    return answer

height = [165, 170, 175, 180, 184]
k = 175
ret = solution(height, k)
print("함수의 반환값은 ", ret, "입니다.")