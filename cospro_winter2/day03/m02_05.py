#빈도(출현 회수)를 구하는 함수 빈칸 채우기
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter

#가장 많은 출연 회수 구하기
def func_b(arr):
    ret = 0
    for i in arr:
        if ret < i:
            ret = i
    return ret

#가장 적은 출연 회수 구하기
def func_c(arr):
    ret = func_b(arr)
    for i in arr:
        if i != 0 and ret > i:
            ret = i
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 1, 1, 1, 1]
ret = solution(arr)
print(ret)
