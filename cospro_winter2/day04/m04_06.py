#화면 내 이동시 x, y가 같은 위치의 개수 구하는 함수 수정하기
def solution(input):
    answer = 0
    x = 0
    y = 0
    for i in input:
        if i == 'w': y -= 1
        elif i == 's': y += 1
        elif i == 'a': x -= 1
        if x == y: answer += 1
    answer += 1
    return answer

input = "wsadsdwsasd"
ret = solution(input)
print(ret)