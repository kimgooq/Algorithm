# 중복 신고는 1 반환
# 신고 받은 횟수가 담긴 리스트 생성
# 신고 받은 횟수가 k번 이상이라면 해당 신고자에게 알림

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    # report_unique = []
    report_unique = set(report)
    report_processed = []
    report_count = [0]*len(id_list)

    answer = [0]*len(id_list)

    # 중복값 제거, set()으로도 진행 가능
    # for i in report:
    #     if i not in report_unique:
    #         report_unique.append(i)

    # reporting, reported 나누기
    for i in report_unique:
        report_processed.append(i.split())

    # id_list의 인덱스와 동일하게 신고 횟수 정의
    for reporting, reported in report_processed:
        report_count[id_list.index(reported)] += 1

    # k번 이상 reported 경우의 reporting 횟수 정의
    for reporting, reported in report_processed:
        if(report_count[id_list.index(reported)] >= k):
            answer[id_list.index(reporting)] += 1

    return answer


answer = solution(id_list, report, k)
print(answer)
