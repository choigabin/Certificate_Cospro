#무게를 재기 위해 필요한 추의 개수를 구하는 함수 빈칸 채우기
def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total

def solution(arr, payload):
    answer = 0
    sum = func_a(arr)
    if sum >= payload:
        arr.sort()
        arr.reverse()
        weight = 0
        for i in range(len(arr)):
            diff = payload - weight
            if arr[i] <= diff:
                weight += arr[i]
                answer += 1
        if weight != payload:
            answer = 0
    return answer

arr = [2, 3, 5, 7, 13, 17, 19, 23]
payload = 25
ret = solution(arr, payload)
print(ret)

