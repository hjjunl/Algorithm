import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    print("First:",scoville)

    while scoville[0]<K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
            answer+=1
        except Exception:
            return -1

    return answer
a=[1, 2, 3, 9, 10, 12,2,3]
print(solution([1, 2, 3, 9, 10, 12],7))
print(heapq.heapify(a))
print(a)