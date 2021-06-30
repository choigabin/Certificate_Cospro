#개구리가 징검다리를 건널 때 점프하는 횟수를 구하는 함수를 수정하기
def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current < n: #current가 n보다 작다면,
        current += stones[current]
        cnt += 1
    return cnt

stones = [2, 5, 1, 3, 2, 1]
ret = solution(stones)
print("함수의 반환값은 ", ret, "입니다.")