#학점별 인원수를 구하는 함수의 빈칸 채우기
def solution(scores):
    grade_counter = [0 for i in range(5)]
    for i in scores:
        if i >= 85: #학점이 100-85라면,
            grade_counter[0] += 1 #0번째 요소 1 증가
        elif i >= 70: #학점이 84-70라면,
            grade_counter[1] += 1 #1번재 요소 1 증가
        elif i >= 55: #학점이 69-55라면,
            grade_counter[2] += 1 #2번째 요소 1 증가
        elif i >= 40: #학점이 54-40라면,
            grade_counter[3] += 1 #3번재 요소 1 증가
        else: #그 이하라면,
            grade_counter[4] += 1 #4번째 요소 1 증가
    return grade_counter

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ret = solution(scores)
print(ret)