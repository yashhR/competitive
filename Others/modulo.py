# t = int(input())
# for _ in range(t):
#     size = int(input())
#     s = list(input())
#     days = int(input())
#     people_to_be_isolated = list(map(int, input().split()))
#     isolated_people = set()
#     prev_positions = {}
#     count = 0
#
#     for i in range(len(s)):
#         if s[i] == '1':
#             prev_positions[i] = True
#     count += len(prev_positions)
#     while days > 0:
#         isolated_people.add(people_to_be_isolated.pop(0))
#         new_positions = {}
#         # print(isolated_people)
#         for position in prev_positions.keys():
#             if position + 1 not in isolated_people:
#                 if position == len(s) - 1:
#                     if s[position-1] != '1':
#                         s[position-1] = '1'
#                         new_positions[position-1] = True
#                 else:
#                     if s[position-1] != '1':
#                         s[position-1] = '1'
#                         new_positions[position - 1] = True
#                     if position + 2 not in isolated_people:
#                         if s[position+1] != '1':
#                             s[position+1] = '1'
#                             new_positions[position+1] = True
#             else:
#                 if position != len(s) - 1:
#                     if position + 2 not in isolated_people:
#                         if s[position+1] != '1':
#                             s[position+1] = '1'
#                             new_positions[position+1] = True
#         prev_positions = new_positions
#         count += len(new_positions)
#         # print(''.join(s))
#         days -= 1
#     # count = 0
#     # for i in range(len(s)):
#     #     if s[i] == '1':
#     #         count += 1
#     print(count)
