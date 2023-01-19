
# < Generator>
# def get_odds():
#     for num in range(10):
#         if num % 2:
#             yield num # return 대신 yield 사용시에 generator가 생성됨
#
#
# gener=get_odds()
# count=0
# for x in gener:
#     count +=1
#     if count ==3:
#         print(f'1에서 10 사이의 수 중에 3번째 홀수는 {x}입니다.')


# <decorator 총정리>
# def test(func):
#     def new_func(*args):
#         print('start')
#         result=func(*args)
#         print(func.__name__)
#         print('end')
#         result=result-10
#         return result
#
#     return new_func
#
# def double(func):
#     def real_double(*no):
#         result=func(*no)
#         print(func.__name__)
#         print(result*result)
#         return result*result
#     return real_double
# @test
# @double
# def complicated_number(*args):
#     x=args[0]
#     y=args[1]
#     n=args[2]
#     return x+y-n
#
# print(complicated_number(3,7,2))


# <예외 발생 raise>

# try:
#     raise Exception('help!')
# except Exception as err:
#     print(err) # help! 출력 : err 변수가 help! 를 받음


# 제너레이터 컴프리헨션

# squares=(f'Got {number}' for number in range(10)) # 제너레이터 객체를 반환 : squares
#
# # def squares(): # 단순 제너레이터 함수는 객체를 반환하지 않음
# #     for number in range(10):
# #         note='Got {}'.format(number)
# #         yield note
#
# for i in squares: # generator comprehension 을 통해 바로 객체를 반환 했으므로 별도로 지정하는 과정이 필요 x
#     print(i)
#
# # x=squares() # 따라서 별도로 제너레이터 객체를 지정해주어야 함
# #
# # for i in x: # 제너레이터 객체의 형태로 for문을 통해 순환 가능
# #     print(i)


drinks={
    'a':{1,11,111},
    'b':{2,22,222},
    'c':{3,33,334}
}

for alph,num in drinks.items():
    if 334 in num:
        num.remove(334)
        num.add(333)
        print(num)
    else:
        print(num)
