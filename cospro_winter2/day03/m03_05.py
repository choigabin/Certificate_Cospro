#카드 게임 승자 알아내는 함수 작성하기
def solution(mho_cards, mhe_cards):
    result = -1
    minho = 0
    minhee = 0
    for i in range(len(mho_cards)): #카드 리스트의 길이만큼 포문 돌리기
        if mho_cards[i] > mhe_cards[i]: #요소들 비교하여 민호의 카드 숫자가 민희의 카드숫자보다 크면,
            minho += 1 #민호에게 1점
        elif mho_cards[i] < mhe_cards[i]: #민희의 카드 숫자가 민호의 카드 숫자보다 크다면,
            minhee += 1 #민희에게 1점
    if minho > minhee: #민호 점수가 민희 점수보다 크다면,
        result = 1 #result에 1 담기
    elif minho < minhee: #민희 점수가 민호 점수보다 크다면,
        result = 0 #result에 0 담기
    return result

mho_cards = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13]
mhe_cards = [2, 1, 3, 4, 5, 9, 6, 7, 8, 10, 11, 12, 13]
ret = solution(mho_cards, mhe_cards)
print(ret)