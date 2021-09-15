#프로그래머스 모의고사
def solution(answers):
    answer = []
    arr1=[ 1, 2, 3, 4, 5]
    arr2=[2, 1, 2, 3, 2, 4, 2, 5]
    arr3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count=[0,0,0]
    for idx, an in enumerate(answers):
        if an==arr1[idx%len(arr1)]:
            count[0]+=1
        if an==arr2[idx%len(arr2)]:
            count[1]+=1
        if an==arr3[idx%len(arr3)]:
            count[2]+=1

    for i, a in enumerate(count):
        if max(count)==a:
            answer.append(i+1)
    return answer

print(solution([2, 1, 2, 3, 2, 4, 2, 5,1, 2,3, 3, 1, 1, 2, 2, 4, 4, 5, 5]))