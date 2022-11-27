from collections import defaultdict


def solution(id_list, report, k):

    dic = defaultdict(int)

    # 신고한자와 당한자가 string 임으로 index로 처리하기 위하여 dic을 활용하여 인덱스로 변환
    for idx, id in enumerate(id_list):
        dic[id] = idx 

    # 신고자와 신고 당한자의 index list 초기화
    reported = [[False for _ in range(len(id_list))]
                for _ in range(len(id_list))]

    # 신고당한자의 신고횟수 초기화
    reported_num = [0 for _ in range(len(id_list))]

    for s in report:
        user, report_user = s.split(' ')

        # 신고한 id
        user = dic[user]

        # 신고당한 id
        report_user = dic[report_user]

        # 이미 신고당한자의 index list에서 신고한자의 index가 있으면 건너띄기 (한번만 신고가 가능함으로)
        if reported[report_user][user]:
            continue

        # 신고당한자의 index list에서 신고한자의 index 값에 true
        reported[report_user][user] = True

        # 신고당한자의 신고횟수 += 1
        reported_num[report_user] += 1

    # 정답을 출력하기 위하여 초기화
    answer = [0 for _ in range(len(id_list))]

    for idx, num in enumerate(reported_num):
        # 정지허용횟수를 넘지 않았으면 패스
        if num < k:
            continue

        # 정지허용횟수를 넘긴 user index중에서 신고자 해당 인덱스의 값의 카운트를 +1 
        for i in range(len(id_list)):
            if reported[idx][i]:
                answer[i] += 1

    return answer




# # id_list = ["con", "ryan"]
# # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# # k = 3

def solution__(id_list, report, k):

    dic = {}

    for idx, id in enumerate(id_list):
        dic[id] = idx

    report_list = [[False for _ in range(len(id_list))] for _ in range(len(id_list))]
    report_num = [0] * len(id_list)

    for repo in report:
        reporter, reported = repo.split(' ')

        reporter = dic[reporter]
        reported = dic[reported]

        if report_list[reported][reporter]:
            continue
        else:
            report_list[reported][reporter] = True
            report_num[reported] += 1

    answer = [0] * len(id_list)

    for idx, num in enumerate(report_num):
        if num < k:
            continue
        else:
            for i in range(len(id_list)):
                if report_list[idx][i]:
                    answer[i] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

answer = solution__(id_list, report, k)
print(answer)