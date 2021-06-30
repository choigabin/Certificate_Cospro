#3게 사면 추가 하나는 50% 할인 행사의 금액을 계산하는 함수의 빈칸 채우기
def solution(arr):
    answer = 0
    for i in range(len(arr)):
        price = arr[i] #가격
        if (i+1) % 4 == 0: #4번째는 반값
            price //= 2 #반값으로
        answer += price
    return answer

arr = [100, 500, 200, 400, 300]
ret = solution(arr)
print(ret)