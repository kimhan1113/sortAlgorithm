from collections import deque


def solution_(cachesize: int, cities: list) -> int:

    # 캐시 사이즈가 0 인경우는 전부 * 5를 해줘서 리턴
    if cachesize == 0:
        return len(cities) * 5

    # queue 자료구조
    cache_list = deque()
    answer = 0

    for city in cities:

        # 전부 문자열 통일
        lower_city = city.lower()

        # 캐시에 값이 없을 때
        if lower_city not in cache_list:

            answer += 5
            # 캐시 사이즈가 꽉찬 경우
            if cachesize <= len(cache_list):
                cache_list.popleft()
                cache_list.append(lower_city)

            # 캐시에 여분이 있는 경우
            else:
                cache_list.append(lower_city)

        # LRU 알고리즘에 따라 한번 갱신을 위하여 remove append 활용
        else:
            answer += 1
            cache_list.remove(lower_city)
            cache_list.append(lower_city)

    return answer


cities = ["Jeju", "Pangyo", "Seoul", "Jeju",
          "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cache_size = 3

answer = solution_(cache_size, cities)
print(answer)


def solution(cacheSize, cities):

    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = dict()

    for i, city in enumerate(cities):
        city = city.lower()

        if cache.__contains__(city):
            answer += 1
            cache[city] = i
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.update({city: i})
            else:
                remove_oldest_city(cache, len(cities))
                cache.update({city: i})

    return answer


def remove_oldest_city(cache: dict, maxIdx: int):
    oldest_city = None
    oldest_city_idx = maxIdx

    for city in cache.keys():
        if cache[city] < oldest_city_idx:
            oldest_city_idx = cache[city]
            oldest_city = city

    if oldest_city:
        del cache[oldest_city]
