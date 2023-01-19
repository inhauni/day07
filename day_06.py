# 전역 함수

# g =1
#
# def print_global():
#     print(g)
#
# print(g)
# print_global() #두개 다 출력 됨


def print_global():
    g = 1
    print(g)
#
# print_global()
# print(g) # Error 발생 'g' 는 전역변수가 아니므로 (지역변수), 함수 밖에선 보이지 않는다
#
# g=1
# def change_print_global():
#     global g # 이 함수에서 사용하는 g는 전역변수 g라는 것을 알려주는 함수
#     print(g)
#     g=2  # 전역변수 g의 값을 2로 바꿈
#     print(g)
#
# change_print_global()
# print_global()
# print(g) # 2가 출력


