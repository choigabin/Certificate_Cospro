#방문객 수의 차이를 구하는 함수의 빈칸 채우기
def func_a(arr, num):
    ret = []
    for i in arr:
        #arr리스트에서 num을 제외하고 복사
        if i != num:
            ret.append(i)
    return ret

#두 갓의 차이를 반환하는 함수
def func_b(a, b):
    if a > b:
        return a - b
    else:
        return b - a

#arr 리스트 요소 중 최댓값을 반환하는 함수
def func_c(arr):
    ret = -1
    for i in arr:
        if ret < i:
            ret = i
    return ret

def solution(visitor):
    max_first = func_c(visitor) #가장 많은 방문객수
    visitor_removed = func_a(visitor, max_first) #젤 큰 값이 제거된 리스트
    max_second = func_c(visitor_removed) #가장 많은 방문객수
    answer = func_b(max_first, max_second) #구한 값의 차이
    return answer

visitor = [1, 3, 2, 4, 5, 3, 6, 3, 7, 4, 6, 7]
ret = solution(visitor)
print(ret)