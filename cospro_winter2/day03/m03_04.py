#페인트 칠하는 데 걸리는 시간을 구하는 함수 빈칸 채우기
def solution(walls):
    answer = 0
    painted_walls = 0
    hour = 1
    while painted_walls < walls: #painted_walls이 walls보다 작다면,
        painted_walls = (hour) + (hour // 2) + (hour // 4)
        hour += 1
    answer = hour - 1
    return answer

walls = 5
ret = solution(walls)
print(ret)