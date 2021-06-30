#축구화 주문 수량 구하는 함수 완성하기
def solution(shoes_size):
    answer = [0 for _ in range(6)]
    for i in shoes_size: #사이즈의 리스트만큼 포문 돌리기
        if i == "7": #사이즈가 7이라면,
            answer[0] += 1 #0번째 요소에 1 증가
        elif i == "7.5": #사이즈가 7.5라면,
            answer[1] += 1 #1번째 요소에 1 증가
        elif i == "8": #사이즈가 8이라면,
            answer[2] += 1 #2번째 요소에 1 증가
        elif i == "8.5": #사이즈가 8.5라면,
            answer[3] += 1 #3번째 요소에 1 증가
        elif i == "9": #사이즈가 9라면,
            answer[4] += 1 #4번째 요소에 1 증가
        elif i == "9.5": #사이즈가 9.5라면,
            answer[5] += 1 #5번째 요소에 1 증가
    return answer

#사이즈를 담은 리스트를 매개변수로
shoes_size = ["7", "7.5", "8", "8.5", "9", "9.5"]
ret = solution(shoes_size)
print(ret)