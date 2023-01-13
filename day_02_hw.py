
#문제 1
import random

guess = int(input("1에서 10까지의 정수 중 하나를 입력하세요 : "))
secret = random.randint(1, 10)
if guess > secret:
    print(f'{guess} is too high')
elif guess < secret:
    print(f'{guess} is too low')
else:
    print(f'{guess} is just right')
