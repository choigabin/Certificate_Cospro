#거꾸로 읽어도 같은 팰린드롬을 확인하는 함수 수정하기
def solution(sentence):
    str = ''
    for c in sentence:
        #온점도 아니고 공백도 아니라면,
        if c != '.' and c != '':
            #str에 넣기
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True

sentence = "reacecar."
ret = solution(sentence)
print("함수의 반환값은 ", ret, "입니다.")