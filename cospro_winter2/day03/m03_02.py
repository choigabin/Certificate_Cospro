#예산을 배분하기 위한 금액을 구하는 함수 빈칸 채우기
#리스트의 모든 요소들의 합 구하기
def func_a(arr):
    total = 0
    for i in arr: #리스트의 길이만큼 포문 돌리기
        total += i #요소를 total에 누적
    return total

def solution(total, arr):
    result = []
    req_total = func_a(arr) #매개변수로 받은 arr 리스트 요소들의 합
    for i in arr: #arr 리스트의 길이만큼 포문 돌리기
        if req_total > total: #req_total 이 total보다 크다면,
            result.append(total // len(arr)) #total // len(arr)을 result 리스트에 추가
        else: #total이 req_total보다 작거나 같다면,
            result.append(i) #i를 result 리스트에 추가
    return result

total = 100
arr = [20, 20, 30, 40]
ret = solution(total, arr)
print(ret)