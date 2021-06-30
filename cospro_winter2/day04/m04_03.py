#통학 버스 왕복 회수 구하는 함수 작성하기
def solution(student, apts):
    result = 0
    total = 0
    for i in student:
        total += i
    result = total // 2
    if total % 12 != 0:
        resutl +=
    return result

student = [2, 5, 4, 7, 8, 2]
ret = solution(student, len(student))
print(ret)