# 새로운 아이디 추천
new_id = "=.="


def solution(new_id):
    answer = ''

    # 소문자 치환
    new_id = new_id.lower()

    # 특정 특수문자 외 전부 삭제
    # re import시
    # new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    for i in new_id:
        if(i.isalnum() or i in "-_."):
            answer += i

    # ".."시 "."로 치환
    # new_id = re.sub('\.+', '.', new_id)
    while (".." in answer):
        answer = answer.replace("..", ".")

    # 처음, 끝 "."일 경우 삭제, answer가 비었을 경우 고려
    #
    if(len(answer) > 0 and answer[0] == "."):
        answer = answer[1:]
    if(len(answer) > 0 and answer[-1] == "."):
        answer = answer[:-1]

    # 비어있을 경우 "a"
    if(answer == ""):
        answer = "a"

    # 16자 이상 시 15자까지, 다만 마지막 "."일 경우 삭제
    if(len(answer) >= 16):
        answer = answer[:15]
        if(answer[-1] == "."):
            answer = answer[:-1]

    # 2자 이하일 경우, 마지막 글자를 덧붙임
    if(len(answer) <= 2):

        answer += answer[-1] * (3-len(answer))

    return answer


answer = solution(new_id)

print(answer)
