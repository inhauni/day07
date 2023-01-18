# None

# def do_nothing():
#     pass

# print(do_nothing())

# mamamoo =['화사','솔라','휘인','문별']

# # print(mamamoo.pop()) # 삭제 할 값 리턴 후 삭제
# print(mamamoo.remove('문별')) # 삭제만 하고 리턴하지 않음 -> None 출력 none: 아무 것도 없다
# print(mamamoo) #문별을 제외한 list가 출력됨


def calculate_fee(*args):

    '''
    [놀이공원 요금계산 프로그램]
    :param args: 나이
    :return: 총 지불 요금
    '''

    total = 0
    for age in args:
       if age >= 19: #adult
           total= total+10000
       else:
           total=total+3000

    return total

print(calculate_fee(20,25,25))
print(calculate_fee(10,7,52,43))