# 제너레이터 함수

# def a():
#     yield 1
#     yield 2
#     yield 3
#  # yield는 반환하면서 함수를 종료시키지 않고 계속 진행한다 = 함수 진행 중간에 값을 반환한다 (return은 함수를 stop하고 종료시킨다)
# def b():
#     return 1 # stop itertation (함수 종결)
#     return 2
#     return 3 #this code is unreachable (because return 1 후에 뒤에 부분은 종료)
#
# print(a(),b()) #generator는 이렇게 출력할 수 없다
#
# for i in a(): # a()는 generator 객체
#     print(i)
# for i in a():
#     print(i) # 이전 상태를 기억하지 못하고 다시 반복

# <decorator>

def document_info(func):
    def new_function(*args,**kwargs):
        print('실행중인 함수: ',func.__name__)
        print('위치 기반 인자들: ',args)
        print('키워드 기반 인자들: ', kwargs)
        result =func(*args,**kwargs)
        print('실행결과: ',result)
        return result
    return new_function

#자동 입력

@document_info
def sub_int(a, b):
    return a+b

print(sub_int(3,5))


@document_info
def squares(n):
    return n*n

print(squares(5))
