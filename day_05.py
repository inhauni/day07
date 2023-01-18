# None

# def do_nothing():
#     pass

# print(do_nothing())

# mamamoo =['화사','솔라','휘인','문별']

# # print(mamamoo.pop()) # 삭제 할 값 리턴 후 삭제
# print(mamamoo.remove('문별')) # 삭제만 하고 리턴하지 않음 -> None 출력 none: 아무 것도 없다
# print(mamamoo) #문별을 제외한 list가 출력됨

import random

# def calculate_fee(*args):
#
#     '''
#     [놀이공원 요금계산 프로그램]
#     :param args: 나이
#     :return: 총 지불 요금
#     '''
#
#     total = 0
#     for age in args:
#        if age >= 19: #adult
#            total= total+10000
#        else:
#            total=total+3000
#
#     return total

# print(calculate_fee(20,25,25))
# print(calculate_fee(10,7,52,43))

# def calculate_fee(args): # *args는 list를 하나의 튜플로 묶어버리니까 19(int)와 ([list])형태의 (튜플리스트)를 비교할 수 없다 ->Error 발생
# # def calculate_fee(args)-> list: #반환하는 return값의 타입을 지정
#
#     '''
#     [놀이공원 요금계산 프로그램]
#     :param args: ages in list
#     :return: 전체 인원 수, 어른 수, 아이 수, 지불할 입장료
#     '''
#
#     total = 0
#     adult = 0
#     kid = 0
#     for age in args:
#        if age >= 19: #adult
#            total= total+10000
#            adult += 1
#
#        else:
#            total=total+3000
#            kid += 1
#
#     return [len(args), adult, kid, total]
#
#
#
# member=int(input('입장 인원 수 : '))
#
# ages=[random.randint(1,60) for age in range(member)] #comprehension
# # ages=[]
# # for i in range(member):
# #     age=random.randint(1,100)
# #     ages.append(age)
# print(ages)
# result=calculate_fee(ages)
#
# print(f'{result[0]}명 방문 하셨고 어른{result[1]}명, 아이{result[2]}명, 따라서 총 요금은 {result[-1]}원 입니다.')



def calculate_fee(args)->dict:

    '''
    [놀이공원 요금계산 프로그램]
    :param args: ages in list
    :return: {'no_of_people':전체 인원 수, 'adult':어른 수, 'kid':아이 수, 'tatal':지불할 입장료}
    '''

    total = 0
    adult = 0
    kid = 0
    for age in args:
       if age >= 19: #adult
           total= total+10000
           adult += 1

       else:
           total=total+3000
           kid += 1

    return {'no_of_people':len(args), 'adult':adult, 'kid':kid, 'total':total}



member=int(input('입장 인원 수 : '))

ages=[random.randint(1,60) for age in range(member)] #comprehension
# ages=[]
# for i in range(member):
#     age=random.randint(1,100)
#     ages.append(a
result=calculate_fee(ages)

print(f"{result['no_of_people']}명 방문 하셨고 어른{result['adult']}명, 아이{result['kid']}명, 따라서 총 요금은 {result['total']}원 입니다.")

