#이름에 특정 문자가 포함된 개수를 구하는 함수 수정하기
def solution(name_list):
    answer = 0
    for name in name_list: #리스트의 길이만큼 포문
        for char in name: #한 문자열의 길이만큼 포문
            #A, K가 있다면, answer에 1 증가
            #없으면 -1(true)로 처리
            if char.find('A') > -1 or char.find('K') > -1:
                answer += 1
                break
    return answer

name = ["Adios", "Kichboard Association", "google"]
ret = solution(name)
print(ret)