# Error

# def div_calc(a,b):
#     '''
#     나눗셈
#     :param a: 실수
#     :param b: 실수
#     :return: 계산 결과
#     '''
#
#     return a / b
#
# print(div_calc(15,3))
# print(div_calc(15,0)) # ZeroDivisionError

# <예외 처리>
try :
    expr = input('분자 분모 입력 (띄어쓰기로 구분) : ').split()
    print(int(expr[0])/int(expr[1]))


   # 발생 가능한 에러 : ZeroDivisionError , ValueError , IndexError, etc..
except ValueError as err:
    print(f'{err}, 숫자를 입력해주세요!')
except ZeroDivisionError as err:
    print(f'{err}, 분모에 0이 올 수 없습니다!')
except IndexError as err:
    print(f'{err}, 인덱스의 범위에 문제가 있습니다!')
except Exception as other: # 기타 발생할 수 있는 모든 예외들
    print(f'{other}, 예외 발생')

else: # 예외가 발생하지 않았을 때 동작
    print('프로그램 정상',end=' ') #밑의 finally까지 함께 실행되어 '프로그램 정상 종료' 출력

finally: # 예외 발생 여부와 상관 없이 무조건 실행
    print('종료') # 오류 발생시 예외 출력과 finally만 실행되어 '종료'만 출력
