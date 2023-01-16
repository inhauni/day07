#while

while True: #무한루프
    dan = int(input('Dan : '))
    if 1 < dan < 10:
        i = 1
        while i < 10:
            print('{0}*{1} ={2}'.format(dan, i, dan * i))
            i += 1
        break #여기에 break를 넣지 않으면 dan*9까지 반복 후 다시 무한루프 초기로 돌아가서 dan을 입력 받는다
    else:
        print('2에서 9의 값을 다시 입력하시오.')


while True:
    stuff =input('string to capitalize[type q to quit] : ')
    if stuff== 'q':
        break
    print(stuff.capitalize())

