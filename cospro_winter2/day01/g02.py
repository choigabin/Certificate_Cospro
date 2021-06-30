#상품 구매 금액을 구하는 함수 완성
import math
#매개변수로 금액, 등급받기
def solution(price, grade):
    #만약 등급이 S라면,
    if(grade == "S"):
        #minus 변수에 price(상품금액)의 5%(할인율) 넣기
        minus = price * 0.05
        #price(상품금액) - minus(할인금액)을 answer에 넣기
        answer = price - minus
    #만약 등급이 G라면,
    elif (grade == "G"):
        # minus 변수에 price(상품금액)의 10%(할인율) 넣기
        minus = price * 0.1
        # price(상품금액) - minus(할인금액)을 answer에 넣기
        answer = price - minus
    #만약 등급이 V라면,
    elif (grade == "V"):
        # minus 변수에 price(상품금액)의 15%(할인율) 넣기
        minus = price * 0.15
        # price(상품금액) - minus(할인금액)을 answer에 넣기
        answer = price - minus
    #금액은 정수이므로, 정수로 변환시킨 answer(최종금액) 리턴
    return int(answer)

price1 = 2500
grade1 = "V"
#등급이 V이고, 구매한 금액이 2500
ret = solution(price1, grade1)
print("함수의  반환값은 ", ret, "입니다.")