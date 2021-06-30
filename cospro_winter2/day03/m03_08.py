#문자열 내의 지정하는 문자들이 있는지 확인하는 함수 수정하기
def solution(password, key):
    answer = 0
    match_cnt = 0
    for k in key: #key 문자열의 길이만큼 포문 돌리기
        for p in password: #password 문자열의 길이만큼 포문 돌리기
            if k == p: #k와 p가 같다면,
                match_cnt += 1 #match_cnt 1 증가
                break
    if match_cnt >= len(key):
        answer = 1
    return answer

password = "1234lsa korean uk"
key = "k l u"
ret = solution(password, key)
print(ret)