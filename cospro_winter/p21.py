#if문
def solution(score):
    if score > 80:
        print("81 이상일 때")
    elif score > 60:
        print("61부터 80 사이일 때")
    elif score > 40:
        print("41부터 60 사이일 때")
    elif score > 20:
        print("21부터 40 사이일 때")
    else:
        print("20 이하일 때")

score = 75
ret = solution(score)
print(ret)