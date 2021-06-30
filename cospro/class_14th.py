def solution(score):
    answer = [0] * len(score)
    rank = dict()
    sorted_score = sorted(score, reverse=True)
    for idx, 점수 in enumerate(sorted_score):
        if 점수 not in rank:
            rank[점수] = idx + 1
    for i in range(len(score)):
        answer[i] = rank[score[i]]
    return answer

score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
