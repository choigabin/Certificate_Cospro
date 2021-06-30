#옷 사이즈가 담긴 리스트에 그 치수의 옷 개수를 담아 리턴
import math
#매개변수로 사이즈가 담긴 리스트 받기
def solution(shirt_size):
    answer = [0] * 6
    sizelist = ["XS", "S", "M", "L", "XL", "XXL"]
    #매개변수로 받은 리스트의 길이만큼 포문돌리기
    for i in range(len(shirt_size)):
        #생성한 sizelist의 길이만큼 포문돌리기
        for j in range(len(sizelist)):
            #탐색과정인 i와 sizelist[j]가 같다면,
            if (shirt_size[i] == sizelist[j]):
                #answer[j]에 1 누적
                answer[j] += 1
                break
    return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)
print("함수의 반환값은 ", ret, "입니다")