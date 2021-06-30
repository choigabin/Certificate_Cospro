#1부터 number까지 369게임을 올바르게 진행했을 경우 박수를 총 몇번 쳤는지 리턴
def solution(number):
    count = 0
    #1부터 number까지
    for i in range(1, number+1):
        current = i
        temp = count
        while current != 0:
            #마지막 자릿수가 3, 6, 9인 경우
            if (current % 10 == 3 or current % 10 == 6 or current % 10 == 9):
                count += 1
                print("짝 ", end=' ')
            #자릿수를 하나하나씩 줄이는 역할
            current = current // 10
        if temp == count:
            print(i, end='')
        print("", end='')
    print("")
    return count

number = 20
ret = solution(number)
print("함수의 반환값은 ", ret, "입니다.")