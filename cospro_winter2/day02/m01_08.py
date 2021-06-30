#거꾸로 읽어도 같은 회문을 확인하는 함수 수정하기
def solution(sentence):
    filtered = []
    for s in sentence:
        if s != '' and s != '.': #s가 공백이거나, 온점이면,
            filtered.append(s)
    before = ''.join(filtered) #리스트를 문자열로 변환
    print(before)
    filtered.reverse()
    after = ''.join(filtered)
    print(after)
    return before == after

sentence = "r  ace c.a.r"
ret = solution(sentence)
print(ret)