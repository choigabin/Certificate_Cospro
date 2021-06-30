#축구장 임대료를 구하는 함수 빈칸 채우기
def solution(n, price):
    games =  n*(n-1) // 2 #게임수
    per_day = n // 2 #2팀이 하루에 한 경기
    answer = (games // per_day) * price
    return answer

teams = 7
price = 100000
ret = solution(teams, price)
print(ret)