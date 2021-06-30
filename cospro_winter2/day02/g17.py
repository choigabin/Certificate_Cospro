def solution(s):
    s_lst = list(s) #문자열을 리스트로
    n = len(s)
    for i in range(n): #리스트의 길이만큼 포문 돌리기
        if s_lst[i] == 'a': #i가 a라면,
            s_lst[i] = 'z' #a를 z로 변경
        elif s_lst[i] == 'z':
            s_lst[i] = 'a'
    return "".join(s_lst) #리스트를 문자열로

name = 'james'
ret = solution(name)
print("함수의 반환값은 ", ret, "입니다.")