
def is_convertible(uid, bid):

    if len(uid) != len(bid):
        return False

    for i, ch in enumerate(uid):
        if bid[i] == "*":
            continue
        elif ch != bid[i]:
            return False

    return True        



def solution(user_id, banned_id):
    answer = 0
    return answer


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]   
banned_id = ["fr*d*", "abc1**"]
result = 2

answer = solution(user_id, banned_id)