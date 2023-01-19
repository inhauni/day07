# <예외 만들기>

try :
    # raise Exception("쉬는 시간!")
    raise TypeError('타입에러') # Excetion 이 other로 받아서 출력
    expr = input('분자 분모 입력 (띄어쓰기로 구분) : ').split()
    print(int(expr[0])/int(expr[1]))



except ValueError as err:
    print(f'{err}, 숫자를 입력해주세요!')
except ZeroDivisionError as err:
    print(f'{err}, 분모에 0이 올 수 없습니다!')
except IndexError as err:
    print(f'{err}, 인덱스의 범위에 문제가 있습니다!')
except Exception as other:
    print(f'{other}, 예외 발생')

else:
    print('프로그램 정상',end=' ')

finally:
    print('종료')