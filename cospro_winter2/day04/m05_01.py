#도착지까지 충전 횟수를 구하는 함수 작성하기
def solution(arr):
    answer = 0
    total = 0

    for i in arr:
        total += i

    answer = total//40

    if total%40 != 0:
        answer += 1

    return answer-1

다시해

arr = [20, 10, 30, 30, 20, 10]
ret = solution(arr)
print(ret)
