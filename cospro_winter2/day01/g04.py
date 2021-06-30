#빈도를 구하는 함수의 빈칸 채우기
#arr 리스트 안에 몇개의 자연수가 있는지 counter에 저장
def func_a(arr):
    #counter[1]에 1의 빈도를 저장
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

#리스트 속에 가장 많이 존재하는 자연수 구하기
def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

#리스트 속에 가장 적게 존재하는 자연수 구하기
def func_c(arr):
    ret = 1001
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

#매개변수로 자연수가 들어있는 리스트 arr 받기
def solution(arr):
    #카운터는 각 수들의 빈도수가 저장된 리스트
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 4, 1, 3, 3, 2, 3, 2]
ret = solution(arr)
print("함수의 반환값은 ", ret, "입니다.")