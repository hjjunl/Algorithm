from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    loc = [i for i in range(len(priorities))]
    result = []
    while len(priorities)!=0:
        if priorities[0] == max(priorities):
            priorities.popleft()
            result.append(loc.pop(0))
        else:
            priorities.append(priorities.popleft())
            loc.append(loc.pop(0))
    return result.index(location) + 1

print(solution([1, 1, 9, 1, 1, 1], 0))