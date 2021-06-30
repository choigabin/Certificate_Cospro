#카드 숫자 조합하여 홀수의 개수를 구하는 함수 빈칸 채우기
def solution(cards):
    answer = 0
    for i in range(3):
        for k in range(i+1, 5):
            for m in range(k+1, 5):
                if (cards[i] + cards[k] + cards[m]) % 2  == 1
                    answer += 1
    return answer

cards = [3, 5, 2, 7, 6]
ret = solution(cards)
print(ret)
