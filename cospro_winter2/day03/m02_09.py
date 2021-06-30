#제품 포장을 위한 포장상자의 개수를 구하는 함수 수정하기
def solution(orders):
    answer = 0
    size = 0
    for o in orders:
        for i in range(6):
            if o[i] != 0: #해당 사이즈의 주문이 있으면
                size += ((i+1)**2)*(o[i]) #수량을 곱하기
    print(size, size // 36)
    answer = size // 36
    if size % 36 != 0:
        answer += 1
    return answer

orders = [[0, 0, 4, 0, 1, 1], [7, 5, 1, 0, 1, 0]]
ret = solution(orders)
print(ret)