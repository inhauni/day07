# 재귀함수
# factorial


def factorial_iter(n):
    '''
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: int type의 팩토리얼 계산 결과 값
    '''

    result = 1

    for k in range(1,n+1):
        result= result*k

    return result

print(factorial_iter(5))


def factorial_recu(n):
    '''
    재귀함수 사용한 factorial 함수
    :param n: n!
    :return: 자기 자신을 호출
    '''

    if n == 1:
        return 1 # 함수 종료 조건
    else:
        return factorial_recu(n-1) * n


print(factorial_recu(5))