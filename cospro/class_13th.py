#당첨자의 시작번호를 리턴
def solution(ladders, win):
   answer = 0
   player = [1, 2, 3, 4, 5, 6]
   for e in ladders:
       temp = player[e[0]-1]
       player [e[0]-1] = player[0[1]-1]
       player [e[1]-1] = temp
   answer = player[win-1]
   return answer

ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]]
win = 3
ret = solution(ladders, win)
print("solution 함수의 반환 값은", ret, "입니다.")



#공강 시간이 몇 시간인지 리턴
def func_a(time_table):
   answer = 0
   for i, t in reversed(list(enumerate(time_table))):
       if t == 1:
           answer = i
           break
   return answer

def func_b(time_table, class1, class2):
   answer = 0
   for i in range(class1, class2):
       if time_table[i] == 0:
           answer += 1
   return answer

def func_c(time_table):
   answer = 0
   for i, t in enumerate(time_table):
       if t == 1:
           answer = i
           break
   return answer

def solution(time_table):
   answer = 0
   # 1.가장 첫 수업 시작시각을 구합니다.
   first_class = func_c(time_table)
   # 2.가장 마지막 수업 시작시각을 구합니다.
   last_class = func_a(time_table)
   # 3.1과 2 사이에서 수업이 비는 시간을 셉니다.
   answer = func_b(time_table, class1, class2)
   return answer

time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
ret = solution(time_table)
print("solution 함수의 반환 값은", ret, "입니다.")



#운전자들의 총 벌금이 얼마인지 합산하여 리턴
def solution(speed, cars):
   answer = 0
   for x in cars:
       if x >= speed * 11 / 10 and x < speed * 12 / 10:
           answer += 3
       elif x >= 12/10 and x < 13/10:
           answer += 5
       elif x >= 13/10:
           answer += 7
   return answer

speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)
print("solution 함수의 반환 값은", ret, "입니다.")



#각 종목에서 획득한 점수를 합산하여 리턴
def solution(taekwondo, running, shooting):
   answer = 0
   if taekwondo >= 25:
      answer += 250
   else:
      answer += taekwondo * 8
   answer += 250 + (60 - running) * 5
   count = 0
   for s in shooting:
      answer += s
      if s == 10:
         count += 1
   if count >= 7:
      answer += 100
   return answer

taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)
print("solution 함수의 반환 값은", ret, "입니다.")



#a일장과 b일장이 동시에 열리는 날이 몇일인지 리턴
def solution(a, b):
   answer = 0
   for i in range(1, b + 1):
       if (a * i) % b == 0:
           answer = b * i
           break
   return answer

a = 4
b = 6
ret = solution(a, b)
print("solution 함수의 반환 값은", ret, "입니다.")



#주어진 평균값이 나올 수 있는 과목의 점수를 리턴
def solution(korean, english):
   answer = 0
   math = 210 - korean - english
   if math > 100:
       answer = -1
   else:
       answer = math
   return answer

korean = 70
english = 60
print("solution 함수의 반환 값은", ret, "입니다.")
