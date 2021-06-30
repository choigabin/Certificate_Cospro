#이름에 특정문자가 들어가있는 사람을 구하는 함수 수정하기
def solution(name_list):
    answer = 0
    for name in name_list: #리스트의 길이만큼 포문 돌리기
        for n in name: #각 이름의 길이만큼 포문 돌리기
            if n == 'j' or n == 'k': #이름에 j, k가 있다면,
                answer += 1 #answer에 1 증가
                break
    return answer

names = ['james', 'kim john', 'jokin']
ret = solution(names)
print("함수의 반환값은 ", ret, "입니다.")