from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
check(10)
def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist=list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))
    answer = len(set(answer))

    return answer
print(solution("274"))


