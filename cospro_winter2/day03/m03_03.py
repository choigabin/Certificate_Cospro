#가장 많이 같은 반을 보낸 학생을 찾는 함수 수정하기
def solution(table):
    answer = 0
    max = 0
    for i in range(1, len(table)): #행(학생)
        sum = 0
        for k in range(5): #열(학년)
            teacher = table[0][k]
            student = table[i][k]
            if teacher == student:
                sum += 1
        if max < sum:
            max = sum
            print(i, "번 학생이 선생님과 가장 많은 같은 반")
            answer = i
    return answer

table = [[2, 6, 1, 7, 3], [2, 9, 4, 6, 8], [6, 3, 4, 7, 1], [7, 7, 1, 1, 2], [8, 6, 9, 7, 3], [4, 6, 5, 9, 2]]
ret = solution(table)
print(ret)

