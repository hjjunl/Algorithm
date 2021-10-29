import math
def solution(progresses, speeds):
    answer = []
    # new_progress = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    new_progress=[]
    answer.append(1)
    l = len(progresses)
    for i in range(l):
        if (100 - progresses[i]) % speeds[i] != 0:
            new_progress.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            new_progress.append((100 - progresses[i]) // speeds[i])
    for i in range(l-1):# 0, 1  7 3 9
        if new_progress[i] < new_progress[i+1]:
            count = 1
            if i+1 != l:
                answer.append(count)
        if new_progress[i] >= new_progress[i+1]:
            answer[-1] += 1
            new_progress[i+1]=new_progress[i]

    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))