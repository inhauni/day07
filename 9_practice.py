# 9.1
# import copy
#
#
# def good():
#     return ['Harry', 'Ron', 'Hermione']
#
# print(good())
#
#
# a_list=[number for number in range(1, 6) if number %2 ==1]
# print(a_list)

# 9.2
#
# count=0
# def get_odds():
#     for number in range(10):
#         if number % 2: # 0이 아닐 경우
#         # if number %2 ==0 :
#         #     continue
#         # else:
#             yield number

# ranger=get_odds()

# count = 0 # 전역 변수(global)

# for x in ranger:
#     count+=1
#     if count == 3:
#         print(x)


# <if not generator>
# def get_odds():
#     for number in range(10):
#         if number % 2: # 0이 아닐 경우
#         # if number %2 ==0 :
#         #     continue
#         # else:
#             return number # 1이 return 되고 종료
#
# print(get_odds())


# 9.3

def test(func):
    def new_func(*args):
        print('start')
        result = func(*args)
        print('end')
        return result
    return new_func

@test
def example_f(a,b):
    print(a+b)
    return (a+b)


print(example_f(3, 7))


# 9.4

class OopsException(Exception):
    pass

try:
    raise OopsException

except OopsException:
    print('Caught an oops')


# < 'panic' 출력>
# class UppercaseException(Exception):
#     pass

# words=['eenie','meenie','miny','MO']
#
# try:
#     for word in words:
#         if word.isupper():
#             raise UppercaseException('panic')
#
# except UppercaseException as exc:
#     print(exc)




