

def document_info(func):
    def new_function(*args,**kwargs):
        print('실행중인 함수: ',func.__name__)
        print('위치 기반 인자들: ',args)
        print('키워드 기반 인자들: ', kwargs)
        result =func(*args,**kwargs)
        print('실행결과: ',result)
        return result
    return new_function


def square_it(func):
    def new_function(*args,**kwargs):
        result=func(*args,**kwargs)
        return result * result
    return new_function

@document_info
@square_it
def add_int(a,b):
    return a+b

print(add_int(3,5)) # 이 때 print 함수는 return 값을 출력
# add_int(3,5) : 이거는 return 값이 출력되지 않음
@square_it
@document_info
def add_int(a,b):
    return a+b

print(add_int(3,5))