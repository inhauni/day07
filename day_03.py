#while

# while True: #무한루프
#     dan = int(input('Dan : '))
#     if 1 < dan < 10:
#         i = 1
#         while i < 10:
#             print('{0}*{1} ={2}'.format(dan, i, dan * i))
#             i += 1
#         break #여기에 break를 넣지 않으면 dan*9까지 반복 후 다시 무한루프 초기로 돌아가서 dan을 입력 받는다
#     else:
#         print('2에서 9의 값을 다시 입력하시오.')

#
# while True:
#     stuff =input('string to capitalize[type q to quit] : ')
#     if stuff== 'q':
#         break
#     print(stuff.capitalize())
#
# while True:
#     value =input("Integer , please [q to quit] : ")
#     if value == 'q':
#         break
#     number=int(value)
#     if number % 2 == 0:
#         continue
#     print(f'{number} squared is {number*number}')
#
# numbers=[1,3,5]
# position =0
# while position<len(numbers):
#     number =numbers[position]
#     if number % 2 ==0 :
#         print(f'Found even number :{number}')
#         break
#     position += 1
# else:
#     print('No even number found')


#for
#
# word ='thud'
#
# for letter in word: #word 라는 문자열을 한 글자씩 letter라는 변수에 넣어 출력
#     print(letter)
#
# while True: #무한루프
#     dan = int(input('Dan : '))
#     if 1 < dan < 10:
#         for i in range(1, 10): #while 문 보다 더 간만하게 표현 가능
#             print('{0}*{1}={2}'.format(dan, i, dan*i))
#         break #여기에 break를 넣지 않으면 dan*9까지 반복 후 다시 무한루프 초기로 돌아가서 dan을 입력 받는다
#     else:
#         print('2에서 9의 값을 다시 입력하시오.')


#<예제 : 소수 출력>
while True:

    number = int(input("정수를 입력하시오 : "))
    counts = 0
# <while문 사용>
# k = 1
# while k <= number:
#     if number % k == 0:
#         counts += 1
#     k +=1
# if counts == 2:
#     print(f"{number} is prime number")
# else:
#     print(f'{number} is not prime number')
#
# <if문 사용>
#     for k in range(1,number+1):
#         if number % k == 0:
#             counts += 1
#     if counts == 2:
#         print(f"{number} is prime number")
#     else:
#         print(f'{number} is not prime number')
#         break

# <if문 ver2>
# number = int(input("정수를 입력하시오 : "))
# counts = 0
#
# for k in range(2, number): #1과 자기자신을 루프에서 뺐을 때 , 0으로 나눠떨어지는 것이 있으면 소수가 x : 이때 소수가 아닐 경우 count값이 변하고
#     if number % k == 0:
#         counts += 1
# if counts: #count값이 변하였을 경우
#     print(f'{number} is not prime number')
# else: #count값이 변하지 않았을 경우 ( 0일 경우)
#     print(f"{number} is prime number")
#
# <if문 ver3>

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

