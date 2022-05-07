# 미확인 숫자는 0
# 0 제외 중복 확인

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]


def solution(lottos, win_nums):
    # 0 정렬 후 개수 파악 및 삭제 -> count() 사용으로 대체
    # lottos.sort(reverse=False)
    # lottos_processed = lottos[:]
    # for i in lottos:
    #     if(i == 0):
    #         lottos_processed.remove(0)
    #     else:
    #         break
    # zero = 6-len(lottos_processed)

    zero = lottos.count(0)

    correct = [i for i in lottos if i in win_nums]

    worst = 7 - len(correct)
    best = worst - zero
    if(worst == 7):
        worst = 6
    if(best == 7):
        best = 6
    answer = [best, worst]

    return answer


answer = solution(lottos, win_nums)
print(answer)
