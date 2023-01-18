# 일반적인 Function

import random

# def process(no_lists,f):
#     for n in no_lists:
#         print(f(n))
# def squares(n):
#     '''
#
#     제곱 함수
#     :param n: 정수
#     :return: 정수(integer)
#     '''
#
#     return n*n


#Lambda
def process(no_lists,f): # f에 lambda x: x*x 라는 익명함수(람다함수)가 대입 됨
    for n in no_lists:
        print(f(n))



numbers=[random.randint(1, 10) for i in range(5)]
print(numbers)

process(numbers, lambda x:x*x) # 람다라는 익명 함수 : x를 대입 시에 x*x를 retrun


