# function : prime number
def isprime(n):
    '''

    :param n: integer number (정수)
    :return: True or False (소수일 때는 True를 return 해줌)
    '''

    if n <= 1: # 1은 소수가 아니므로 False 반환
        return False
    for k in range(2, n): # 소수가 아닌 경우
        if n % k == 0:
            return False
    else: # 소수일 경우
        # print(i, end=' ') 함수 하나는 한 가지 역할에 충실 해야 함 : 답변(True or False)과 출력을 동시에 할 수 없다
        return True



start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start:
    start, end = end, start

for i in range(start, end+1):
    if isprime(i):
        print(i, end=' ')
