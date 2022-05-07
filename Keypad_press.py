# left 1 4 7
# right 3 6 9
# dictionary에 번호 및 해당 위치 지정

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"


def thumb_by_distance(num_pos, R_pos, L_pos, hand):
    dis_right = abs(num_pos[0] - R_pos[0]) + abs(num_pos[1]-R_pos[1])
    dis_left = abs(num_pos[0] - L_pos[0]) + abs(num_pos[1]-L_pos[1])

    if (dis_right == dis_left):
        if(hand == "right"):
            thumb = "R"
        else:
            thumb = "L"
    elif (dis_right > dis_left):
        thumb = "L"
    else:
        thumb = "R"

    return thumb


def solution(numbers, hand):
    num_dic = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (
        1, 2), "7": (2, 0), "8": (2, 1), "9": (2, 2), "*": (3, 0), "0": (3, 1), "#": (3, 2)}

    R = "#"
    L = "*"
    input_list = []
    for i in numbers:
        if(i in [3, 6, 9]):
            input_list.append("R")
            R = i
        elif (i in [1, 4, 7]):
            input_list.append("L")
            L = i
        # 4 3
        else:
            num_pos = num_dic[str(i)]
            R_pos = num_dic[str(R)]
            L_pos = num_dic[str(L)]
            thumb = thumb_by_distance(num_pos, R_pos, L_pos, hand)
            if(thumb == "R"):
                input_list.append("R")
                R = i
            else:
                input_list.append("L")
                L = i

    return "".join(input_list)


answer = solution(numbers, hand)

print(answer)
