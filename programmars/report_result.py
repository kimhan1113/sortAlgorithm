from collections import defaultdict


# def solution(id_list, report, k):

#     dic = defaultdict(int)

#     for idx, id in enumerate(id_list):
#         dic[id] = idx

#     reported = [[False for _ in range(len(id_list))]
#                 for _ in range(len(id_list))]
#     reported_num = [0 for _ in range(len(id_list))]

#     for s in report:
#         user, report_user = s.split(' ')

#         # 신고한 id
#         user = dic[user]

#         # 신고당한 id
#         report_user = dic[report_user]

#         if reported[report_user][user]:
#             continue
#         reported[report_user][user] = True
#         reported_num[report_user] += 1

#     answer = [0 for _ in range(len(id_list))]

#     for idx, num in enumerate(reported_num):
#         if num < k:
#             continue
#         for i in range(len(id_list)):
#             if reported[idx][i]:
#                 answer[i] += 1

#     return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3


# answer = solution(id_list, report, k)
# print(answer)


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported = [[False for _ in range(len(id_list))]
                for _ in range(len(id_list))]
    reported_num = [0 for _ in range(len(id_list))]

    dic = dict()

    for i, name in enumerate(id_list):
        dic[name] = i

    for repo in report:
        reporter, reported_name = repo.split(' ')

        reporter = dic[reporter]
        reported_name = dic[reported_name]

        if reported[reported_name][reporter]:
            continue

        reported[reported_name][reporter] = True
        reported_num[reported_name] += 1

    for idx, num in enumerate(reported_num):
        if num < k:
            continue

        for i in range(len(id_list)):
            # 정지 당한 idx에서 신고한 i의 값을 +1 해준다
            if reported[idx][i]:
                answer[i] += 1

    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2

# answer = solution(id_list, report, k)
# print(answer)


# def solution(id_list, report, k):

#     reported = [[False for _ in range(len(id_list))]
#                 for _ in range(len(id_list))]

#     answer = []

#     # 신고한 리스트
#     do_lists = defaultdict(list)

#     # 신고받은 리스트
#     get_lists = defaultdict(list)

#     pause_list = []

#     for repo in report:
#         reporter, reported = repo.split(' ')[0], repo.split(' ')[1]

#         if reporter not in get_lists[reported]:
#             get_lists[reported].append(reporter)

#             if len(get_lists[reported]) >= k:
#                 pause_list.append(reported)

#         if reported not in do_lists[reporter]:
#             do_lists[reporter].append(reported)

#     if len(max(get_lists.items())) < k:
#         answer = [0] * len(id_list)
#         return answer

#     for ids in id_list:
#         count = 0
#         for check_id in do_lists[ids]:
#             if check_id in pause_list:
#                 count += 1
#         answer.append(count)

#     return answer


def solution__(id_list, report, k):

    dic = defaultdict(int)

    for i in range(len(id_list)):
        dic[id_list[i]] = i

    reported = [[False for _ in range(len(id_list))]
                for _ in range(len(id_list))]
    reported_num = [0 for _ in range(len(id_list))]
    answer = [0 for _ in range(len(id_list))]

    for i, repo in enumerate(report):

        reporter, reported_name = repo.split()

        reported_name = dic[reported_name]
        reporter = dic[reporter]

        if reported[reported_name][reporter]:
            continue

        reported[reported_name][reporter] = True
        reported_num[reported_name] += 1

    for idx, num in enumerate(reported_num):

        if num < k:
            continue

        for i, name in enumerate(id_list):
            if reported[idx][i]:
                answer[i] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

answer = solution__(id_list, report, k)
print(answer)
