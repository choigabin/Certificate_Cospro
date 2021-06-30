#관세를 매긴 금액을 구하는 함수 수정하기
def solution(price, grade):
    if(grade == "S"): #지역이 S라면
        answer = price + (price*0.05) #5%의 관세 추가
    elif(grade == "G"): #지역이 G라면
        answer = price + (price*0.1) #10%의 관세 추가
    elif(grade == "V"): #지역이 V라면
        answer = price + (price*0.15) #15%의 관세 추가

    return int(answer)

price = 1300
grade = "G"
ret = solution(price, grade)
print(ret)
