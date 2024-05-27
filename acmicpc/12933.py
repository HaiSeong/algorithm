# line = input()
#
# quack = {
#     'q': 0,
#     'u': 1,
#     'a': 2,
#     'c': 3,
#     'k': 4
# }
# #
# # visited = [False] * len(line)
# #
# # def dfs(now, q):
# #     visited[now] = True
# #     next = now + 1
# #     while next < len(line) and :
# #
# #
#
#
#
# count = {i:0 for i in range(5)}
# answer = {}
#
# starts = []
# ends = []
#
# for i, c in enumerate(line):
#     if quack[c] == 0:
#         starts.append(i)
#         count[quack[c]] += 1
#     else:
#         if count[quack[c] - 1] > 0:
#             count[quack[c] - 1] -= 1
#             count[quack[c]] += 1
#             if (quack[c] == 4):
#                 ends.append(i)
#
#     # print(c, count)
#
# # print()
# # print(starts)
# # print(ends)
#
# if len(starts) != len(ends):
#     print(-1)
# else:
#     lst = list(zip(starts, ends))
#     lst_ = lst[0]
#     answer_set = set([lst_[1]])
#
#     for s, e in lst[1:]:
#         min_a = min(answer_set)
#         if min_a > s:
#             answer_set.add(e)
#         else:
#             answer_set.remove(min_a)
#             answer_set.add(e)
#
#     print(len(answer_set))
#
#
# '''
# qu_ac_k________
# __q__u__a__ck__
# _______q_ua__ck
#
# qu_ac_kq_ua__ck
# __q__u__a__ck__
# '''
from collections import Counter

line = input()
visited = [False] * len(line)
quack = {
    'q': 0,
    'u': 1,
    'a': 2,
    'c': 3,
    'k': 4
}


def dfs(now, q):
    # print(now, line[now])
    visited[now] = True

    for next in range(now + 1, len(line)):
        if quack[line[next]] == (q + 1) % 5 and not visited[next]:
            dfs(next, (q + 1) % 5)
            break
    else:
        if q != 4:
            print(-1)
            exit(0)


c = Counter(line)
if len(c.keys()) != 5 or len(set(c.values())) != 1:
    print(-1)
    exit(0)

answer = 0
for i in range(len(line)):
    if not visited[i] and line[i] == 'q':
        # print('-' * 20)
        dfs(i, 0)
        answer += 1

print(answer)