#점수의 총합에서 최고점수와 최저점수를 뺄셈하는 함수의 빈칸 채우기
def func_a(s):
    s.sort() #리스트 정렬
    return s[len(s)-1], s[0]

#점수의 총합 구하는 함수
def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

#최고점수와 최저 점수를 빼는 함수
def solution(scores):
    sum = func_b(s)
    max, min = func_a(s)
    return sum - max - min

s = [10,20,50,90,30,40]
ret = solution(s)
print(ret)
