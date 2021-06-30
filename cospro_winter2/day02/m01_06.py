#교차점의 개수를 구하는 함수 빈칸 채우기
def solution(left_rings):
    answer = 0
    for i in range(len(left_rings)):
        #수평보다 위로 연결되어 교차 발생
        if left_rings[i] <= i;
            for k in range(i):
                if left_rings[k] > left_rings[i]:
                    answer += 1
    return answer

left_rings = [1,4,2,5,3]
ret = solution(left_rings)
print(ret)
