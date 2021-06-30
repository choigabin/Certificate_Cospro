#정수에 3, 6, 9가 포함되어있는지 확인하는 함수의 빈칸 채우기
def solution(number):
    count = 0
    #1부터 number까지 범위
    for i in range(1, number+1):
        current = i
        while current != 0:
            unit = current % 10 #일의 자리 구하기
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
            #일의 자리수 떼기 (다음처리할 수 계산)
            current //= 10
    return count

number = 36
ret = solution(number)
print(ret)