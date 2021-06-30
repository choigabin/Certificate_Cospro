#수업 별 신청자 인원수 구하는 함수 수정하기
def solution(arr):
    answer = [0, 0, 0] #과목의 수는 3개
    for i in range(3):
        for k in rnage(4):
            answer[i] += arr[i*4+k] #과목별로 4개씩
    return answer

arr = [8, 5, 3, 5, 6, 7, 3, 4, 5, 6, 7, 8]
ret = solution(arr)
print(ret)