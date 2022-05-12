board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    result_list = []
    removed = 0
    # tranpose 불필요 >> for문 i, j로 list[j][i] 계산
    board_transpose = list(map(list, zip(*board)))
    for grab in moves:
        grab_line = grab - 1
        for i in range(len(board_transpose[grab_line])):
            if(board_transpose[grab_line][i] == 0):
                pass
            elif(board_transpose[grab_line][i] != 0):
                doll_num = board_transpose[grab_line][i]
                board_transpose[grab_line][i] = 0
                result_list.append(doll_num)
                if(len(result_list) != 1 and result_list[-1] == result_list[-2]):
                    del result_list[-2:]
                    removed += 2
                break
    return removed


answer = solution(board, moves)

print(answer)
