# prime number v0.6

number = int(input("input number : "))
is_prime = True

for k in range(2, number):
    if number % k == 0:
        is_prime = False
        break
    print(k)

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')



number = int(input("정수를 입력하시오 : "))
is_prime =True # 소수일 경우

for k in range(2, number):
    if number % k ==0:
        is_prime =False #소수가 아닐 경우
        break # 소수가 아닐 경우 바로 탈출 ( 소수가 아닌 수를 입력했을 때 공간 절약 가능)
if is_prime:
    print(f"{number} is prime number")
else:
    print(f"{number} is prime number")


