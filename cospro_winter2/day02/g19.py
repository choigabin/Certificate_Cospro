#거스름돈을 리턴하는 함수 작성
def solution(price, money):
    sum = 0
    for i in range(len(price)): #가격 리스트의 길이만큼 포문 돌리기
        sum += price[i] #리스트의 모든 요소들의 합 구하기

    if sum <= money: #가진 money가 sum보다 크다면
        answer = money - sum #money - sum 계산하기
        return answer
    else: #money가 sum보다 작다면,
        return -1 #-1 리턴

price = [2100, 3200, 2100, 800]
money = 5000
ret = solution(price, money)
print("함수의 반환값은 ", ret, "입니다.")