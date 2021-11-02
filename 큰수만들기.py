# def solution(number, k):
#     answer = ''
#     num = []
#     count = 0
#     # for i in number:
#     #     num.append(int(i))
#     num = list(number)
#     new = []
#     m=0
#     print(num)
#     for i in range(len(num)-1):
#         for a in range(i+1, i+1+k-count):
#             if count < k:
#                 if int(num[i]) < int(num[a]) and int(num[i])!=-1:
#                     print("num[i]값", num[i])
#                     print("num[a]값", num[a])
#                     count += 1
#                     num[i] = -1
#                     new.append(i)
#                     print(count)
#                     print(num)
#     while -1 in num:
#         num.remove(-1)
#     print(num)
#     answer = "".join(map(str,num))
#     print(answer)
#     return answer
# solution("4177252841", 4)

def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        print(answer)

    return ''.join(answer[:len(answer) - k])
print(solution("1231234", 3))