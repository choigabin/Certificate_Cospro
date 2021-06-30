#학100 > scores >= 85 solution(scores):
def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores: #스코어의 길이만큼 포문 돌리기
        if 100 >= x >= 85: #100점 - 85점이라면,
            grade_counter[0] += 1
        elif 84 > x >= 70: #84점 - 70점이라면,
            grade_counter[1] += 1
        elif 69 > x >= 55: #69점 - 55점이라면,
            grade_counter[2] += 1
        elif 54 > x >= 40: #54점 - 40점이라면,
            grade_counter[3] += 1
        else: #40점 미만이라면,
            grade_counter[4] += 1

    return grade_counter

scores = [50, 95, 70, 65, 90, 80, 60]
ret = solution(scores)
print("함수의 반환값은 ", ret, "입니다.")