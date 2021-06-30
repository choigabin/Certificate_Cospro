#대괄호 쌍의 개수를 세는 함수 빈칸 채우기
def func_a(s):
    answer = False
    cnt = 0
    for i in s:
        if i == '[':
            cnt += 1
        if i == ']':
            cnt -= 1
    if cnt == 0:
        answer = True
    return answer

def solution(string):
    answer = 0
    if not func_a(string):
        return -1
    for i in string:
        if i == ']':
            answer += 1
    return answer

string = "[[][]]"
ret = solution(string)
print(ret)