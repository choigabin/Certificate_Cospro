#거스름돈 계산하는 함수 작성
def solution(price, money):
    sum = 0
    for i in range(len(price)): #가격리스트의 길이만큼 포문 돌리기
        sum += price[i] #리스트의 모든 요소의 합 구하기

    if sum <= money: #가진 돈이 계산해야할 돈보다 많다면,
        answer = money - sum #계산
        return answer
    else: #가진 돈이 계산해야할 돈보다 작다면,
        return -1 #-1 리턴

price = [2100, 3200, 2100, 800]
money = 1000
ret = solution(price, money)
print(ret)