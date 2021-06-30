#중복되는 문자를 제거하는 함수 수정하기
def solution(characters):
    result = ""
    result += characters[0]
    #1부터 characters의 길이만큼 포문 돌리기
    for i in range(1, len(characters)):
        #characters[i-1]와 characters[i]가 같지 않다면,
        if characters[i - 1] != characters[i]:
            #result에 character의 i값 넣기
            result += characters[i]
    return result

characters = "senteeencccccccceeee"
ret = solution(characters)
print("함수의 변환값은 ", ret, "입니다.")