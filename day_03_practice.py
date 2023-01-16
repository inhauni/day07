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
numbers=[1,3,5]
position =0
while position<len(numbers):
    number =numbers[position]
    if number % 2 ==0 :
        print(f'Found even number :{number}')
        break
    position += 1
else:
    print('No even number found')

