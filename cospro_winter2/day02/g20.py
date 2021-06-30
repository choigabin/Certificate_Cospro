def solution(arr, k):
    answer = 0
    #arr의 모든 요소를 저장할 1차 리스트
    temp = []

    for a in arr:
        for b in a:
            temp.append(b)

    for i in range(len(arr):
        for j in range(4):
            temp.append(arr[i][j])

    #배열 정렬
    temp.sort()
    answer = temp[k-1]

    return answer

arr = [[5, 12, 4, 31], [24, 13, 11, 2], [43, 44, 19, 26], [33, 65, 20, 21]]
k = 4
ret = solution(arr, k)
print("함수의 반환값은 ", ret, "입니다.")
