#수강 대상자 수를 구하는 함수 고치기
#매개변수로 socres 받기
def solution(scores):
    count = 0
    for s in scores:
        #650점 이상 800점 미만의 성적을 취득한 학생이 있다면,
        if 650 <= s < 800:
            #count 증가
            count += 1
    return count

#학생들의 점수를 담은 리스트
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)
print("함수의 반환값은 ", ret, "입니다.")