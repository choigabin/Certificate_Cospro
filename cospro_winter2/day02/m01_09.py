#중복되는 문자를 제거하는 함수 수정하기
def solution(characters):
    result = [characters[0]] #처음 문자 1개를 대입
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i])
    return ''.join(result)

sentence = "senteeeeenccccceeeee"
ret = solution(sentence)
print(ret)