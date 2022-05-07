s = "23four5six7six"


def solution(s):
    num_to_eng = [["zero", "0"], ["one", "1"], ["two", "2"], ["three", "3"],
                  ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]

    for e, n in num_to_eng:
        if (e in s):
            s = s.replace(e, n)

    answer = int(s)

    return answer


answer = solution(s)
print(answer)
