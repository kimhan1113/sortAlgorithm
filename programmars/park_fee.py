from collections import defaultdict
from math import ceil

def solution(fees, records):
    total = defaultdict(int)
    parked = dict()

    for record in records:
        time, num, status = record.split(" ")
        HH, MM = time.split(":")
        time = int(HH) * 60 + int(MM)
        
        if status == "IN":
            parked[num] = time
        elif status == "OUT":
            total[num] += time - parked[num]
            del parked[num]

    last = 23 * 60 + 59
    for num, time in parked.items():
        total[num] += last - time
    
    result = [(num, time) for num, time in total.items()]
    result.sort(key=lambda x:x[0])

    answer = []

    for num, time in result:
        if time < fees[0]:
            answer.append(fees[1])
        else:
            time -= fees[0]
            answer.append(fees[1] + ceil(time / fees[2]) * fees[3])

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = [14600, 34400, 5000]