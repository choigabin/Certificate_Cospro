#야구 게임의 볼 판정 함수 수정하기
def solution(a, b):
    result = [0, 0]
    for i in range(3): #a값의 위치
        temp = b
        for k in range(3): #b값의 위치
            if a % 10 == temp % 10: #숫자가 같다면,
                if i == k: #위치가 같다면,
                    result[0] += 1
                else: #위치가 다르다면,
                    result[1] += 1
            temp //= 10 #비교할 b의 자리수를 위로 이동
        a //= 10
    return result

a = 356
b = 356
ret = solution(a, b)
print(ret)