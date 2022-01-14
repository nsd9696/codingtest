#2309
# list = [int(input()) for i in range(9)]

# total = sum(list)

# for i in range(9):
#     for j in range(i+1,9):
#         if 100 == total - (list[i] + list[j]): 
#             num1,num2=list[i],list[j]

#             list.remove(num1)
#             list.remove(num2)
#             list.sort() # 오름차순 정리

#             for i in range(len(list)):
#                print(list[i])
#             break

#     if len(list)<9:
#         break

#1339
# import string
# num_words = int(input())
# words = [input() for i in range(num_words)]

# word_dict = {}
# alphabets= list(string.ascii_uppercase)
# for i in alphabets:
#     word_dict[i] = 0

# for w in words:
#     for i,a in enumerate(w[::-1]):
#         word_dict[a] += 10**i
# sorted_dict = sorted(word_dict.items(),key=lambda x: x[1],reverse=True)
# answer = 0
# for i,v in enumerate(sorted_dict[:9]):
#     num = 9-i
#     answer += v[1] * num
# print(answer)
