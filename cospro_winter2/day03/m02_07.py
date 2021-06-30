#문자열 내 특정 문자를 바꾸는 함수 수정하기
def solution(s):
    answer = []
    for c in s:
        if '0' <= c <= '9':
            n = ord('i') - ord(c)
            c = chr(n)
        answer.append(c)
    return ''.join(answer)

s = "ab1c3b"
ret = solution(s)
print(ret)

i = ord('i')
y = ord('0')
g = ord('9')
print(i, y, g)