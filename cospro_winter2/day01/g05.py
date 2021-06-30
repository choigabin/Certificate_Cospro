#리스트 요소들의 순서를 뒤집는 함수의 빈칸 채우기
def solution(arr):
    left, right = 0, len(arr) - 1
    #2개씩 짝 지어 교환하기 때문에 right가 left보다 커야함
    while left < right:
        # 양 쪽 끝끼리 변경
        arr[left], arr[right] = arr[right], arr[left]
        #left ------>
        left += 1
        #right <-----
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)
print("함수의 반환값은 ", ret, "입니다.")