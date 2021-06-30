#문자열들을 처리하는 시간 구하는 함수 수정하기
def solution(strings):
    result = 0
    for s in strings:
        length = len(s)
        result += (length // 4)
        if length % 4 != 0: #남는 문자가 3개 이하일때 한번 처리
            result += 1
    return result

strings = ["1234", "1234", "1234"]
ret = solution(strings)
print(ret)