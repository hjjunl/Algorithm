from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.pop()
        idx+=1
        if idx < len(numbers):
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                print(answer)
                answer +=1
        print(queue)
    return answer

solution([1, 1, 1, 1, 1], 3)