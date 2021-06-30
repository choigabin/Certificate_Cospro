#, B, C, D 네 개의 축구팀이 모여 축구대회를 개최
def solution(scores):
    result = [0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            if i != k: #대각선이 아닌 부분 (경기가 가능한)
                result[i] += scores[i][k]*2 #승리 시 승점이 2점
    return result

scores = [[0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
ret = solution(scores)
print(ret)