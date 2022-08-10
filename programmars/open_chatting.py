from collections import defaultdict


def solution(record):
    answer = []
    user_dict = defaultdict(str)

    for i, user in enumerate(record):

        # 0은 command, 1은 userid, 2는 nickname
        user_split = user.split(' ')
        if user_split[0] == "Enter":
            user_dict[user_split[1]] = user_split[2]

        elif user_split[0] == "Leave":
            # user_dict[user_split[1]] = user_dict[user_split[1]] + "_"
            pass

        else:
            user_dict[user_split[1]] = user_split[2]

    for reco in record:
        check = reco.split(' ')
        if check[0] == "Enter":
            answer.append(str(user_dict[check[1]])+"님이 들어왔습니다.")
        elif check[0] == "Leave":
            answer.append(str(user_dict[check[1]])+"님이 나갔습니다.")
        else:
            continue

    # for user in user_dict.keys():
    #     if user_dict[user][-1] == "_":
    #         answer.append(str(user_dict[user].split(" ")[0])+"님이 나갔습니다.")

    #     else:
    #         answer.append(str(user_dict[user].split(" ")[0])+"님이 들어왔습니다.")

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


answer = solution(record)
print(answer)
