# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(lambda: 0)
    total_list = defaultdict(lambda: [])

    for i in range(len(genres)):
        genre_dic[genres[i]] += plays[i]
        print(genre_dic)
        total_list[genres[i]].append((plays[i], i))
        print(total_list)

    assert 1 == 0

    genre_dic = sorted(genre_dic.items(), key=lambda x: x[1], reverse=True)

    for i in total_list:
        total_list[i] = sorted(
            total_list[i], key=lambda x: x[0], reverse=True)[:2]

    while len(genre_dic) > 0:
        genre_max = genre_dic.pop(0)

        for t in total_list:
            if t == genre_max[0]:
                if len(total_list[i]) > 1:
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else:
                    answer.append(total_list[t][0][1])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# solution(genres, plays)


def solution_(genres: list, plays: list) -> list:
    genres_count = defaultdict(lambda: 0)
    genres_idx = defaultdict(list)

    for i, genre in enumerate(genres):
        genres_count[genre] += plays[i]
        genres_idx[genre].append(i)

    hq_count = []

    for genres in genres_count.keys():
        heapq.heappush(hq_count, (-genres_count[genres], genres))


# solution_(genres, plays)

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))
    print(heap)  # (우선 순위, 값)

# print(heap)
