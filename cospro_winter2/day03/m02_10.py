#ISBN 규칙을 확인하는 함수 작성하기
def sum_isbn(isbn):
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2:
            w = 3
        else:
            w = 1
        sum += w * c
    return sum

def solution(isbn):
    print(isbn)
    answer = ''
    sum = sum_isbn(isbn[:-1])
    r = 10 - (sum % 10)
    if r == 10:
        answer = '0'
    else:
        answer = str(r)
    return answer

ret = solution("9788970508122")
print(ret == '2')