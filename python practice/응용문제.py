# #0. 알파벳 노이즈 제가 > 공백구별 정수 더하기
# #sol1
# noised_list= input("알파벳 노이즈가 있는 문장을 입력하세요: ").split()
# filtered_list = []

# for i in noised_list:
#     filtered_str = ""
#     for j in i:
#         if j in list(map(str,range(0,10))):
#             filtered_str += j
#     filtered_list.append(filtered_str)

# filtered_list = map(int, filtered_list)
# print(sum(filtered_list))


# #sol2
# import re

# noised_list = input("알파벳 노이즈가 있는 문장을 입력하세요: ").split()
# unjoined_list = []
# filtered_list = []

# for i in noised_list:
#     x = re.findall(r'\d+', i)
#     unjoined_list.append(x)
# print(unjoined_list)

# for j in unjoined_list:
#     j = "".join(j)
#     filtered_list.append(j)
# print(filtered_list)

# filtered_list = map(int, filtered_list)
# print(sum(filtered_list))

# # sol1
# # for i in range(25):
# #     print(i, end=' ')

# # 2. 0~24까지 정수를 한줄에 5개씩 출력하세요
# # sol1
# for i in range(5):
#     for j in range(5):
#         print(i * 5 + j, end=' ')