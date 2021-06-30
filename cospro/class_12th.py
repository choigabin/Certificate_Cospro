#사용할 수 있는 포인트를 리턴
def solution(point):
   if point < 1000:
       return 0
   return point // 100 * 100
   # return pont-(point%100)

point = 2323
ret = solution(point)
print("solution 함수의 반환 값은", ret, "입니다.")



#기말고사 - 중간고사의 값을 구하고 최댓값과 최솟값 리턴
def func_a(middle_score_list, final_score_list):
    answer = 0
    for middle_score_list, final_score_list in zip(middle_score_list, final_score_list):
        answer = max(answer, final_score_list - middle_score_list)
    return answer

def func_b(middle_score_list, final_score_list):
    answer = 0
    for middle_score_list, final_score_list in zip(middle_score_list, final_score_list):
        answer = min(answer, final_score_list - middle_score_list)
    return answer

def solution(mid_scores, final_scores):
    # 1. 각 학생에 대하여 기말고사 점수에서 중간고사 점수를 뺀 값의 최댓값을 구합니다.
    up = func_a(mid_scores, final_scores)
    # 2. 각 학생에 대하여 기말고사 점수에서 중간고사 점수를 뺀 값의 최소값을 구합니다.
    down = func_b(mid_scores, final_scores)
    # 3. 1번과 2번 과정에서 구한 점수를 리스트에 담아 return 합니다.
    answer = [up, down]
    return answer

mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)
print("solution 함수의 반환 값은", ret, "입니다.")



#과반수를 득표한 후보자의 번호를 리턴
def solution(n, votes):
   arr = [0] * (n + 1)
   for vote in votes:
       arr[vote] += 1

   for i in range(1, n+1):
       if arr[i] > len(votes)/2:
           return i
   return -1

n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)
print("solution 함수의 반환 값은 ", ret2, " 입니다.")



#동서남북이 자신보다 큰 수라면 위험지역으로 판단, 위험지역의 갯수를 리턴
def solution(height):
    count = 0 #위험지역 카운트 변수
    for i in range(len(height)):
        for j in range(len(height)):
            if i > 0: #바로 위 행이 높은 지역이 아니라면
                #왼쪽의 원소가 더 높은 지역이 아니라면
                if not (height[i - 1][j] > height[i][j]):
                    continue
            if j > 0: #오른쪽의 원소가 존재한다면
                #오른쪽의 원소가 더 높은 지역이 아니라면
                if not (height[i][j - 1] > height[i][j]):
                    continue
            if i < len(height) - 1: #위쪽의 원소가 존재한다면
                #위쪽의 원소가 더 높은 지역이 아니라면
                if not (height[i + 1] > height[i][j]):
                    continue
            if j < len(height[i]) - 1:  #아래쪽의 원소가 존재한다면
                #아래쪽의 원소가 더 높은 지역이 아니라면
                if not (height[i][j + 1] > height[i][j]):
                    continue
            count += 1
    return count

height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)
print("solution 함수의 반환 값은", ret, "입니다.")


#커트라인을 넘은 합격자수를 리턴
# import math

def solution(scores, cutline):
   answer = 0
   for score in score_list:
       if score >= cutline:
           answer += 1
   return answer

score_list = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(score_list, cutline)
print("solution 함수의 반환 값은", ret, "입니다.")



